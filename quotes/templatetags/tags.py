from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name):
    request = context.get('request', '')
    url = reverse(url_name)

    return 'active' if request.path == url else ''
