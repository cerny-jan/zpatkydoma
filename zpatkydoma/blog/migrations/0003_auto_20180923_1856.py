# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-23 16:56
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180301_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('title-small', 'Small'), ('title-med', 'Medium'), ('title-large', 'Large'), ('title-extra-large', 'Extra Large')], required=False))])), ('indented_paragraph_block', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'bold', 'italic', 'strikethrough', 'hr', 'link'], icon='pilcrow', label='Indented Text', template='blocks/indented_paragraph_block.html')), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'bold', 'italic', 'strikethrough', 'hr', 'link'], icon='pilcrow', label='Text', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(blank=True, required=False))])), ('landscape_images_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(blank=True, required=False))]), help_text='Add even number of images (it inserts 2 horizontal images on the line)', icon='image', label='Landscape Images', template='blocks/landscape_images_block.html')), ('portrait_images_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(blank=True, required=False))]), help_text='Add 2 images (it inserts 2 vertical images on the line)', icon='image', label='Portrait Images', template='blocks/portrait_images_block.html')), ('image_slider_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))]), help_text='Full width image slider, add at least 4 images', icon='image', label='Image Slider', template='blocks/image_slider_block.html')), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(required=False)), ('author', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='media', template='blocks/embed_block.html')), ('raw_html', wagtail.core.blocks.RawHTMLBlock(help_text='A text area for entering raw HTML which will be rendered unescaped', label='Raw HTML', required=False, template='blocks/raw_html_block.html'))], blank=True, verbose_name='Page body'),
        ),
    ]
