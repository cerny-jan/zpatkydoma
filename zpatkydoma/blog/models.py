import datetime

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.fields import StreamField

from zpatkydoma.base.blocks import BaseStreamBlock


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')


class RelatedPage(models.Model):
    page = ParentalKey('blog.BlogPage', related_name='related_pages')
    related_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    panels = [
        PageChooserPanel('related_page', 'blog.BlogPage'),
    ]

class BlogPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only'
    )
    date_published = models.DateField(
        'Published date', default=datetime.date.today)
    intro = models.CharField(
        max_length=250, help_text='Text to describe the page',)
    body = StreamField(BaseStreamBlock(required=False),
                       verbose_name='Page body', blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('intro', classname="full"),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('date_published'),
            FieldPanel('tags'),
        ], heading='Blog information'),
        InlinePanel('related_pages', label='Related Pages',max_num=3)
    ]

# TO DO otestovat related pages with current code, recreate database

    def get_context(self, request):
        context = super(BlogPage, self).get_context(request)
        tags =self.related_pages.all()
        for tag in tags:
            print(tag.page)
        return context
