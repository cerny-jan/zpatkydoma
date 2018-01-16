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
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.blocks import RichTextBlock

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
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only'
    )
    date_published = models.DateField(
        'Published date', default=datetime.date.today)

    intro = StreamField([
            ('paragraph', RichTextBlock(
            template="blocks/intro_paragraph_block.html",
            features=['bold', 'italic', 'hr', 'link']))
    ])

    body = StreamField(
    BaseStreamBlock(required=False),
                       verbose_name='Page body', blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('intro'),
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('date_published'),
            FieldPanel('tags'),
        ], heading='Blog information'),
        InlinePanel('related_pages', label='Related Pages', max_num=3)
    ]

    def related_pages_columns(self):
        related_pages_count = self.related_pages.all().count()
        if related_pages_count > 2:
            return 4
        elif related_pages_count > 0:
            return 6
        else:
            return None

    # def get_context(self, request):
    #     # Update context to include only published posts, ordered by reverse-chron
    #     context = super(BlogPage, self).get_context(request)
    #
    #
    #     return context


class BlogIndexPage(Page):
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
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        # if not self.promo_page:
        #     self.promo_page = blogpages.first()
        # blogpages = blogpages.not_page(self.promo_page)
        context['blogpages'] = blogpages

        return context

    content_panels = Page.content_panels + [
        PageChooserPanel('promo_page', 'blog.BlogPage'),
    ]
