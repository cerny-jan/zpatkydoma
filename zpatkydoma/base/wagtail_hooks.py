from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from zpatkydoma.blog.models import BlogCategory




class BlogCategoryModelAdmin(ModelAdmin):
    model = BlogCategory
    menu_label = 'Blog Categories'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-bookmark-o'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    # or True to exclude pages of this type from Wagtail's explorer view
    exclude_from_explorer = True
    inspect_view_enabled = True


modeladmin_register(BlogCategoryModelAdmin)
