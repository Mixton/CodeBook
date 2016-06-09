from codebook.lib.http import instance, impose_action, redirect
from codebook.lib.auth import makeUser, authUser, deauthUser
from codebook.lib.auth import getUser, getUserByID
from codebook.lib import openio
from django.http import Http404
from codebook.models import Post, Follow

def guest_index(request):
    return instance(request, "codebook/guest_index.html")

def index(request):
    if not request.user.is_authenticated():
        return guest_index(request)

    follows = Follow.objects.filter(fid = request.user.id)
  
    uPosts = request.user.post_set.filter().order_by('-created')

    uPosts = [post for post in uPosts]
    for follow in follows:
        follow = getUserByID(follow.uid)
        fPosts = follow.post_set.filter().order_by('-created')
        uPosts += [post for post in fPosts]

    uPosts.sort(key=lambda x: str(x.created), reverse=True)

    ctx = { 'posts': uPosts, 'followers': follows }

    return instance(request, "codebook/index.html", ctx)

def register(request):
    reqKeys = ['username', 'email', 'password']
    action = impose_action(request, "users/register.html", reqKeys)
    if action:
        return action

    user = makeUser(request.POST)
    container = openio.Container(user.username).create()
    return auth(request)

def auth(request):
    reqKeys = ['username', 'password']
    action = impose_action(request, "users/auth.html", reqKeys)
    if action:
        return action

    request = authUser(request)
    return redirect("codebook:index")

def deauth(request):
    request = deauthUser(request)
    return redirect("codebook:index")

def follow(request, username):
    user = getUser(username)
    f = Follow.objects.create(uid = user.id, fid = request.user.id)
    f.save()
    return redirect("codebook:user", {'username': username})

def unfollow(request, username):
    user = getUser(username)
    f = Follow.objects.get(uid = user.id, fid = request.user.id)
    f.delete()

    return redirect("codebook:user", {'username': username})

def deactivate(request):
    if request.user.is_authenticated():
        request.user.is_active = False
        request.user.save()
        request = deauthUser(request)
    return instance(request, "users/deactivate.html")

def user(request, username):
    ctx = { 'username': username }

    try:    user = getUser(username)
    except: raise Http404("{} is not a registered user".format(username))

    ctx['posts'] = user.post_set.filter().order_by('-created')

    return instance(request, "users/view.html", ctx)

def post(request, username, pid):
    ctx = { 'username': username }
    user = getUser(username)
    
    userMismatch = username != request.user.username
    try:
        f = Follow.objects.get(uid = user.id, fid = request.user.id)
    except:
        f = None

    if userMismatch and not f:
        return redirect("codebook:user", {'username': username})

    ctx['post'] = user.post_set.get(pk = pid)
    return instance(request, "users/post.html", ctx)

# Create your views here.
