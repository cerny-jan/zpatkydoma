from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from zpatkydoma.blog.models import BlogCategory
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from zpatkydoma.blog.models import BlogPage
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler

from wagtail.core import hooks

# 1. Use the register_rich_text_features hook.
@hooks.register('register_rich_text_features')
def register_strikethrough_feature(features):
    """
    Registering the `strikethrough` feature, which uses the `STRIKETHROUGH` Draft.js inline style type,
    and is stored as HTML with an `<s>` tag.
    """
    feature_name = 'strikethrough'
    type_ = 'STRIKETHROUGH'
    tag = 's'

    # 2. Configure how Draftail handles the feature in its toolbar.
    control = {
        'type': type_,
        'label': 'S',
        'description': 'Strikethrough',
        # This isn’t even required – Draftail has predefined styles for STRIKETHROUGH.
        # 'style': {'textDecoration': 'line-through'},
    }

    # 3. Call register_editor_plugin to register the configuration for Draftail.
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    # 4.configure the content transform from the DB to the editor and back.
    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: tag}},
    }

    # 5. Call register_converter_rule to register the content transformation conversion.
    features.register_converter_rule('contentstate', feature_name, db_conversion)


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('css/custom_admin_editor.css')
    )


class BlogPageModel(ModelAdmin):
    model = BlogPage
    menu_icon = 'form'
    menu_order = 200

    def published_date(self, obj):
        return obj.date_published.strftime('%d-%m-%Y')

    def parent_page(self, obj):
        return obj.get_parent()
    parent_page.admin_order_field = 'url_path'

    list_display = ('title', 'parent_page', 'category',
                    'published_date', 'live')
    list_filter = ('category',)
    search_fields = ('title', 'intro', 'body')
    list_per_page = 30


class BlogCategoryModelAdmin(ModelAdmin):
    model = BlogCategory
    menu_label = 'Blog Categories'  # ditch this to use verbose_name_plural from model
    menu_icon = 'radio-empty'  # change as required
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    # or True to exclude pages of this type from Wagtail's explorer view
    exclude_from_explorer = True
    inspect_view_enabled = True


modeladmin_register(BlogPageModel)
modeladmin_register(BlogCategoryModelAdmin)
