from django import template
from codebook.models import Follow
from codebook.lib.auth import getUser, getUserByID

register = template.Library()

@register.filter
def isFollowing(requestUser, username):
    user = getUser(username)
    try:    Follow.objects.get(uid = user.id, fid = requestUser.id)
    except: return False
    return True

@register.simple_tag
def nameof(follow):
    user = getUserByID(follow.uid)
    return user.username

