from django.http import HttpResponse
from . import api

def index(request):
    return HttpResponse("а")

def register(request):
    return HttpResponse(api.register(request.GET['login'], request.GET['name'], request.GET['password']))

def login(request):
    return HttpResponse(api.login(request.GET['login'], request.GET['password']))

def user(request, s):
    return HttpResponse(api.get_user(s))

def user_add_greenhouse(request, s):
    return HttpResponse(api.user_add_greenhouse(s, request.GET['greenhouse']))

def get_greenhouse(request, id):
    return HttpResponse(api.get_greenhouse(request.GET['session'], id))

def register_greenhouse(request):
    return HttpResponse(api.register_greenhouse())

def greenhouse_state(request, id):
    s = request.GET['session']
    for key in request.GET.dict().keys():
        v = request.GET[key]
        if (key == 'light'):
            api.greenhouse_light(s, id, int(v))
        if (key == 'wind'):
            api.greenhouse_wind(s, id, int(v))
        if (key == 'water'):
            api.greenhouse_water(s, id, int(v))
    return HttpResponse(api.greenhouse_get_state(id))

def greenhouse_history(request, id):
    return HttpResponse(api.greenhouse_history(id))

def greenhouse_history_add(request, id):
    return HttpResponse(api.greenhouse_history_add(id, request.GET['h'], request.GET['w'], request.GET['t']))