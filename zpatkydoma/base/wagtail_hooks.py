from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from zpatkydoma.blog.models import BlogCategory
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from zpatkydoma.blog.models import BlogPage

from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('css/custom_admin_editor.css')
    )


class BlogPageModel(ModelAdmin):
    model = BlogPage
    menu_icon = 'fa-file-text-o '
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
    menu_icon = 'fa-bookmark-o'  # change as required
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    # or True to exclude pages of this type from Wagtail's explorer view
    exclude_from_explorer = True
    inspect_view_enabled = True


modeladmin_register(BlogPageModel)
modeladmin_register(BlogCategoryModelAdmin)
