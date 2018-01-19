from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import (
    StreamFieldPanel,
    PageChooserPanel,
    TabbedInterface,
    ObjectList
)


from .blocks import BaseStreamBlock
from zpatkydoma.blog.models import BlogPage


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

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        blogpages = BlogPage.objects.live().order_by('-date_published')
        if not self.promo_page:
            self.promo_page = blogpages.first()
        blogpages = blogpages.not_page(self.promo_page) if blogpages else blogpages
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        PageChooserPanel('promo_page', 'blog.BlogPage'),
    ]

    settings_panels = []

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='Page Configuration'),
    ])
