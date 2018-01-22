from django import template


register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.assignment_tag(takes_context=True)
def menu(context, calling_page=None):
    menuitems = context['request'].site.root_page.get_children(
    ).live().in_menu()
    for menuitem in menuitems:
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }
