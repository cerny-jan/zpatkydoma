from __future__ import absolute_import, unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.validators import MinValueValidator, MaxValueValidator

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import (
    StreamFieldPanel,
    PageChooserPanel,
    TabbedInterface,
    ObjectList,
    FieldPanel
)
from wagtail.contrib.settings.models import BaseSetting, register_setting


from .blocks import BaseStreamBlock
from zpatkydoma.blog.models import BlogPage


@register_setting(icon='fa-facebook')
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Facebook page URL', blank=True)
    twitter = models.CharField(
        help_text='Twitter username', blank=True, max_length=255,)
    email = models.EmailField(
        help_text='Email address', blank=True)
    instagram = models.URLField(
        help_text='Instagram username', blank=True)


class StandardPage(Page):

    body = StreamField(BaseStreamBlock(required=False), blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]


class HomePage(Page):
    promo_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Promo page that should be on the top',
        verbose_name='Promoted Page'
    )

    posts_per_page = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(
        30)], default=25, help_text='Number of posts shown per page (min  5, max 30)')

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        all_blogpages = BlogPage.objects.live().order_by('-date_published')
        # if the promo_page wasn't set in Admin, use the lastest published page
        if not self.promo_page:
            self.promo_page = all_blogpages.first()
        # don't show the promo page twice
        all_blogpages = all_blogpages.not_page(
            self.promo_page) if all_blogpages else all_blogpages
        paginator = Paginator(all_blogpages, self.posts_per_page)
        page = request.GET.get('page')
        try:
            blogpages = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            blogpages = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            blogpages = paginator.page(paginator.num_pages)
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        PageChooserPanel('promo_page', 'blog.BlogPage'),
    ]

    settings_panels = []

    cofiguration_panels = Page.promote_panels + [
        FieldPanel('posts_per_page')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(cofiguration_panels, heading='Page Configuration'),
    ])
