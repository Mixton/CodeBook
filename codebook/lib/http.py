from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext

def instance(request, route, context = dict()):
    context['request'] = request
    return render(request, route, context)

def redirect(route, args = None):
    return HttpResponseRedirect(reverse(route, kwargs=args))

def missing(keys, params):
    for key in keys:
        if key not in params:
            return key
    return None

def enforce(keys, params):
    miaKey = missing(keys, params)
    if miaKey:
        raise Http404("Required key {} is missing from POST parameters"\
                      .format(miaKey))
    return None

def impose_action(request, route, reqKeys):
    if request.method == 'GET':
        return instance(request, route)
    if request.method != 'POST':
        raise Http404("This script only accepts post and get requests")

    enforce(reqKeys, request.POST)
    return None

