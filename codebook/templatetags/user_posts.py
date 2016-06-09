from django import template
from codebook.lib import openio
from codebook.lib.auth import getUser

register = template.Library()

Container = None
Cache = {}

DataKey = {
    'source': lambda C: C.data,
    'type':   lambda C: C.meta['type'],
    'output': lambda C: C.meta['output']
}

@register.simple_tag(takes_context=True)
def info(context, post, attr):
    if post.uid.id not in Cache:
        Cache[post.uid.id] = dict()

    if post.id not in Cache[post.uid.id]:

        name = post.uid.username

        Container = openio.Container(name)
        Cache[post.uid.id][post.id] = Container.fetch(
                "post/{}".format(post.id)
            , openio.SourceObject)

    return DataKey[attr](Cache[post.uid.id][post.id])

@register.simple_tag
def idof(post):
    return str(post.id)

@register.simple_tag
def dateof(post):
    return str(post.created)[:19]

@register.simple_tag
def nameof(post):
    return post.uid.username

languages = {
    'c': 'c',
    'cpp': 'cpp',
    'py': 'python',
    'pl': 'perl',
    'rb': 'ruby',
}

@register.simple_tag(takes_context=True)
def langof(context, post):
    return languages[info(context, post, 'type')]

slanguages = {
    'c': 'C',
    'cpp': 'C++',
    'py': 'Python',
    'pl': 'Perl',
    'rb': 'Ruby',
}

@register.simple_tag(takes_context=True)
def slangof(context, post):
    return slanguages[info(context, post, 'type')]


