from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def authLink(context):
    if context['request'].user.is_authenticated():
        return "/deauth"
    return "/auth"

@register.simple_tag(takes_context=True)
def authText(context):
    return "Logout" if context['request'].user.is_authenticated() else "Login"

@register.simple_tag(takes_context=True)
def authName(context):
    if context['request'].user.is_authenticated():
        return context['request'].user.username
    return ''

''' Give the current request's user object as the tag value '''
@register.simple_tag(takes_context=True)
def user(context):
    return context['request'].user

''' See if arg object user is authenticated '''
@register.filter
def isAuthed(user):
    return user.is_authenticated() is True

@register.simple_tag
def nameof(user):
    return user.username

