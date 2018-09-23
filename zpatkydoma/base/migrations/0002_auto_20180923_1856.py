# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-23 16:56
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import zpatkydoma.base.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.core.fields.StreamField([('one_columng_block', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('title-small', 'Small'), ('title-med', 'Medium'), ('title-large', 'Large'), ('title-extra-large', 'Extra Large')], required=False))])), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'], icon='pilcrow', label='Text')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(help_text='A text area for entering raw HTML which will be rendered unescaped', label='Raw HTML', required=False, template='blocks/raw_html_block.html'))]))])), ('two_column_block', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('title-small', 'Small'), ('title-med', 'Medium'), ('title-large', 'Large'), ('title-extra-large', 'Extra Large')], required=False))])), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'], icon='pilcrow', label='Text')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(help_text='A text area for entering raw HTML which will be rendered unescaped', label='Raw HTML', required=False, template='blocks/raw_html_block.html'))], icon='arrow-left', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('title-small', 'Small'), ('title-med', 'Medium'), ('title-large', 'Large'), ('title-extra-large', 'Extra Large')], required=False))])), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'], icon='pilcrow', label='Text')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(help_text='A text area for entering raw HTML which will be rendered unescaped', label='Raw HTML', required=False, template='blocks/raw_html_block.html'))], icon='arrow-right', label='Right column content'))])), ('separator_line_block', zpatkydoma.base.blocks.SeparatorLineStaticBlock())], blank=True),
        ),
    ]
