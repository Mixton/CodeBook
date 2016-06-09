from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import Http404

# Reserve these names since we use them as controller routes.
# Users may not register as these names.
reserved = { 'register', 'auth', 'deauth', 'deactivate' }

def makeUser(params):
    if params['username'] in reserved:
        raise Http404("{} is a reserved keyword".format(params['username']))

    user = User.objects.create_user(
            username = params['username'],
            email    = params['email'],
            password = params['password']
        )
    return user

def authUser(request):
    params = request.POST

    user = authenticate(
            username = params['username'],
            password = params['password']
        )

    if not user:
        raise Http404("That user does not exist")
    elif not user.is_active:
        raise Http404("That user account is disabled")

    login(request, user)
    return request

def deauthUser(request):
    if request.user.is_authenticated():
        logout(request)
    return request

def getUser(username):
    return User.objects.get(username = username)

def getUserByID(uid):
    return User.objects.get(id = uid)

