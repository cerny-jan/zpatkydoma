from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


from .blocks import BaseStreamBlock


class StandardPage(Page):
    """
    A generic content page.
    """

    body = StreamField(BaseStreamBlock(required=False), blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
