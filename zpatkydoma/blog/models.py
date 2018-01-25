import datetime

from django.db import models
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.validators import MinValueValidator, MaxValueValidator

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase, Tag

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
    TabbedInterface,
    ObjectList
)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from zpatkydoma.base.blocks import BaseStreamBlock


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    panels = [
        FieldPanel('name')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Blog Categories'


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

    intro = RichTextField(features=['bold', 'italic', 'hr', 'link'])

    body = StreamField(
        BaseStreamBlock(required=False),
        verbose_name='Page body', blank=True)

    date_published = models.DateField(
        'Published date', default=datetime.date.today)

    category = models.ForeignKey(
        'blog.BlogCategory',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    def related_pages_columns(self):
        related_pages_count = self.related_pages.all().count()
        if related_pages_count > 2:
            return 4
        elif related_pages_count > 0:
            return 6
        else:
            return None


    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('intro', classname='full'),
        StreamFieldPanel('body')
    ]

    cofiguration_panels = Page.promote_panels + [
        MultiFieldPanel([
            FieldPanel('date_published'),
            FieldPanel('category', widget=forms.Select),
            FieldPanel('tags'),
            InlinePanel('related_pages',
                        label='Related Pages', max_num=3)
        ], heading='Blog Page Configuration')
    ]

    settings_panels = []

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(cofiguration_panels, heading='Page Configuration'),
    ])

    parent_page_types = ['blog.BlogListPage']
    subpage_types = []

    class Meta:
        verbose_name = 'Blog Page'


class BlogListPage(Page):

    sub_title = models.CharField(blank=True, max_length=255)

    posts_per_page = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(
        30)], default=25, help_text='Number of posts shown per page (min  5, max 30)')

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogListPage, self).get_context(request)
        all_blogpages = self.get_children().live().order_by('-first_published_at')

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

    settings_panels = []

    cofiguration_panels = Page.promote_panels + [
        FieldPanel('posts_per_page')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('sub_title', classname='full')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(cofiguration_panels, heading='Page Configuration'),
    ])

    subpage_types = ['blog.BlogPage']

    class Meta:
        verbose_name = 'Blog List Page'


class BlogTagPage(Page):

    def get_context(self, request):
        tag = request.GET.get('tag')
        if tag:
            blogpages = BlogPage.objects.filter(tags__slug=tag)
        else:
            blogpages = BlogPage.objects.all()
        context = super(BlogTagPage, self).get_context(request)
        context['blogpages'] = blogpages
        context['tag'] = Tag.objects.filter(slug=tag).first()
        return context

    settings_panels = []

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='Page Configuration'),
    ])

    subpage_types = ['blog.BlogPage']

    class Meta:
        verbose_name = 'Blog Tag Page'
