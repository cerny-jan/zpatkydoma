# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-05 17:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import zpatkydoma.base.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, help_text='The footer text is not html escaped', max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Footer Text',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('posts_per_page', models.IntegerField(default=25, help_text='Number of posts shown per page (min  5, max 30)', validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(30)])),
            ],
            options={
                'verbose_name': 'Home Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, help_text='Facebook username', max_length=255, verbose_name='Facebook username')),
                ('facebook_app_id', models.CharField(blank=True, help_text='https://developers.facebook.com/docs/apps/register', max_length=255, verbose_name='Facebook App ID')),
                ('twitter', models.CharField(blank=True, help_text='Twitter username without @', max_length=255, verbose_name='Twitter username')),
                ('email', models.EmailField(blank=True, help_text='Email address', max_length=254)),
                ('instagram', models.CharField(blank=True, help_text='Instagram username', max_length=255, verbose_name='Instagram username')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('sub_title', models.CharField(blank=True, help_text='if a subtitle is used, entire title section of the page will be bigger', max_length=255)),
                ('body', wagtail.core.fields.StreamField((('one_columng_block', wagtail.core.blocks.StructBlock((('column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('title-small', 'Small'), ('title-med', 'Medium'), ('title-large', 'Large'), ('title-extra-large', 'Extra Large')], required=False))))), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'], icon='fa-paragraph', label='Text')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)),)))))),))), ('two_column_block', wagtail.core.blocks.StructBlock((('left_column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('title-small', 'Small'), ('title-med', 'Medium'), ('title-large', 'Large'), ('title-extra-large', 'Extra Large')], required=False))))), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'], icon='fa-paragraph', label='Text')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)),)))), icon='arrow-left', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock((('heading', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('title-small', 'Small'), ('title-med', 'Medium'), ('title-large', 'Large'), ('title-extra-large', 'Extra Large')], required=False))))), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'], icon='fa-paragraph', label='Text')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)),)))), icon='arrow-right', label='Right column content'))))), ('separator_line_block', zpatkydoma.base.blocks.SeparatorLineStaticBlock())), blank=True)),
            ],
            options={
                'verbose_name': 'Standard Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='homepage',
            name='promo_page',
            field=models.ForeignKey(blank=True, help_text='Promo page that should be on the top', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Promoted Page'),
        ),
    ]
