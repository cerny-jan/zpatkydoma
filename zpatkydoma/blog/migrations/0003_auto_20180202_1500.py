# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-02 15:00
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180131_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading_block', wagtail.wagtailcore.blocks.StructBlock((('heading_text', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('title-small', 'Small'), ('title-med', 'Medium'), ('title-large', 'Large'), ('title-extra-large', 'Extra Large')], required=False))))), ('indented_paragraph_block', wagtail.wagtailcore.blocks.RichTextBlock(features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'], icon='fa-paragraph', label='Indented Text', template='blocks/indented_paragraph_block.html')), ('paragraph_block', wagtail.wagtailcore.blocks.RichTextBlock(features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'], icon='fa-paragraph', label='Text', template='blocks/paragraph_block.html')), ('image_block', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.wagtailcore.blocks.CharBlock(blank=True, required=False))))), ('landscape_images_block', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.wagtailcore.blocks.CharBlock(blank=True, required=False)))), help_text='Add even number of images (it inserts 2 images on the line)', icon='image', label='Landscape Images', template='blocks/landscape_images_block.html')), ('portrait_images_block', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('caption', wagtail.wagtailcore.blocks.CharBlock(blank=True, required=False)))), help_text='Add 2 images (it inserts 2 images on the line)', icon='image', label='Landscape Images', template='blocks/portrait_images_block.html')), ('image_slider_block', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)),)), help_text='Full width image slider, add at least 4 images', icon='image', label='Image Slider', template='blocks/image_slider_block.html')), ('block_quote', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('author', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))))), ('embed_block', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html')), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text='A text area for entering raw HTML which will be rendered unescaped', label='Raw HTML', required=False, template='blocks/raw_html_block.html'))), blank=True, verbose_name='Page body'),
        ),
    ]
