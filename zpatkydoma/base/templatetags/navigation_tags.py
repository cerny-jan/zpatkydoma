from django import template


register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.assignment_tag(takes_context=True)
def top_menu(context, calling_page=None):
    menuitems = context['request'].site.root_page.get_children().live().in_menu()
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }
