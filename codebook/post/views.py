from codebook.lib.http import instance, redirect, impose_action
from codebook.lib import code, openio
from codebook.models import Post
from django.http import Http404
from django.utils import timezone

def create(request):
    if not request.user.is_authenticated():
        raise Http404("You must be logged in to create a post")

    reqKeys = ['source', 'type']
    action = impose_action(request, "post/create.html", reqKeys)
    if action:
        return action

    params = request.POST
    username = request.user.username

    try:
        output = code.run(params['source'], params['type'])
    except Exception as exc:
        output = str(exc)

    post = request.user.post_set.create(
            uid = request.user,
            created = timezone.now()
        )
    post.save()
    post.refresh_from_db()

    container = openio.Container(username)
    meta = { 'type': params['type'], 'output': output }
    obj = openio.SourceObject(params['source'], meta)

    container.add(obj, "post/{}".format(post.id))

    return redirect("codebook:index")

def edit(request, pid):
    if not request.user.is_authenticated():
        raise Http404("You must be logged in to edit a post")

    try:
        post = request.user.post_set.get(pk = pid)
    except:
        raise Http404(
                "Post /{}/{} does not exist"\
                .format(request.user.username, pid)
            )

    # Do GET or enforce POST parameters
    reqKeys = ['source', 'type']
    action = impose_action(request, "post/edit.html", reqKeys)
    if action:
        return action

    args = { 'username': request.user.username, 'pid': pid }
    return redirect("codebook:post", args)






