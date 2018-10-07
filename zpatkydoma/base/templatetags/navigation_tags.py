from django import template
from zpatkydoma.base.models import FooterText


register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.simple_tag(takes_context=True)
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


@register.simple_tag(takes_context=True)
def get_footer_text(context):
    footer_text = ""
    if FooterText.objects.first() is not None:
        footer_text = FooterText.objects.first().body

    return {
        'footer_text': footer_text,
    }
