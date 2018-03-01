from __future__ import absolute_import, unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.validators import MinValueValidator, MaxValueValidator

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    PageChooserPanel,
    TabbedInterface,
    ObjectList,
    FieldPanel
)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.snippets.models import register_snippet

from .blocks import BaseStreamBlock, StandardPageStreamBlock
from zpatkydoma.blog.models import BlogPage


@register_setting(icon='fa-facebook')
class SocialMediaSettings(BaseSetting):
    facebook = models.CharField(
            help_text='Facebook username', blank=True, max_length=255, verbose_name='Facebook username')
    facebook_app_id = models.CharField(
        help_text='https://developers.facebook.com/docs/apps/register', blank=True, max_length=255, verbose_name='Facebook App ID')
    twitter = models.CharField(
        help_text='Twitter username without @', blank=True, max_length=255, verbose_name='Twitter username')
    email = models.EmailField(
        help_text='Email address', blank=True)
    instagram = models.CharField(
        help_text='Instagram username', blank=True, max_length=255, verbose_name='Instagram username')


@register_snippet
class FooterText(models.Model):
    body = models.TextField(blank=True, max_length=400, help_text='The footer text is not html escaped')

    panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = 'Footer Text'


class StandardPage(Page):

    sub_title = models.CharField(
        blank=True, max_length=255, help_text='if a subtitle is used, entire title section of the page will be bigger')

    body = StreamField(StandardPageStreamBlock(required=False), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('sub_title', classname='full'),
        StreamFieldPanel('body')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='Page Configuration'),
    ])

    class Meta:
        verbose_name = 'Standard Page'


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
        all_blogpages = BlogPage.objects.live().order_by('-date_published','-last_published_at')
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

    parent_page_types = ['wagtailcore.Page']

    class Meta:
        verbose_name = 'Home Page'
