from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def swap(value):
    return value.swapcase()

@register.filter
@stringfilter
def bold(value):
    return f'<b>{value}</b>'