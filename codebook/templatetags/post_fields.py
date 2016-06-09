from django import template
from codebook.models import Follow
from codebook.lib.auth import getUser
from codebook.lib import openio

register = template.Library()

@register.simple_tag(takes_context=True)
def sourceof(context, obj):
    return obj.data

@register.simple_tag(takes_context=True)
def typeof(context, obj):
    return obj.meta['type']

@register.simple_tag(takes_context=True)
def outputof(context, obj):
    return obj.meta['output']

