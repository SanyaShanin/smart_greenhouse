from smart_greenhouse.models import User, Session, Greenhouse
import json

def user_by_session(session):
    s = Session.objects.filter(identificator=session).first()
    if (s == None):
        return None
    u = User.objects.filter(login=s.login).first()
    return u;

def greenhouse_by_session(session, id):
    u = user_by_session(session)
    if (u == None):
        return None
    gh = u.greenhouses.filter(identificator=id).first()
    return gh


def register(login, name, password):
    if (len(login) < 4 or len(login) > 40):
        return 'login'
    if (len(password) < 4 or len(password) > 40):
        return 'password'
    if (len(name) < 4 or len(name) > 80):
        return 'name'

    u = User.objects.filter(login=login).first()
    if (u != None):
        return 'exists'

    u = User(login = login, name = name)
    u.set_password(password)
    u.save()

    s = Session(login=login)
    s.save()
    return s.identificator

def login(login, password):
    u = User.objects.filter(login=login).first()
    if (u == None):
        return 'invalid'

    if (not u.validate_password(password)):
        return 'invalid'

    s = Session(login=login)
    s.save()
    return s.identificator

def get_user(session):
    u = user_by_session(session)
    if (u == None):
        return 'session'
    return json.dumps(u.get())

def user_add_greenhouse(session, id):
    u = user_by_session(session)
    if (u == None):
        return 'session'
    gh = u.greenhouses.filter(identificator=id).first()
    if (gh != None):
        return 'exists'
    gh = Greenhouse.objects.filter(identificator=id).first()
    if (gh == None):
        return 'greenhouse'

    u.greenhouses.add(gh)
    u.save()
    return 'ok'

def get_greenhouse(session, id):
    gh = greenhouse_by_session(session, id)
    if (gh == None):
        return 'error'
    return json.dumps(gh.get())

def register_greenhouse():
    gh = Greenhouse()
    gh.wind = False
    gh.light = False
    gh.water = False
    gh.save()
    return gh.identificator

def greenhouse_light(session, id, light):
    gh = greenhouse_by_session(session, id)
    if (gh == None):
        return 'error'

    gh.light = light > 0
    gh.save()
    return 'ok'

def greenhouse_wind(session, id, wind):
    gh = greenhouse_by_session(session, id)
    if (gh == None):
        return 'error'

    gh.wind = wind > 0
    gh.save()
    return 'ok'

def greenhouse_water(session, id, water):
    gh = greenhouse_by_session(session, id)
    if (gh == None):
        return 'error'

    gh.water = water > 0
    gh.save()
    return 'ok'

def greenhouse_get_state(id):
    gh = Greenhouse.objects.filter(identificator=id).first()
    if (gh == None):
        return 'exists'

    return json.dumps(gh.get_state())

def greenhouse_history(id):
    gh = Greenhouse.objects.filter(identificator=id).first()
    if (gh == None):
        return 'exists'

    return json.dumps(gh.history)

def greenhouse_history_add(id, h, w, t):
    gh = Greenhouse.objects.filter(identificator=id).first()
    if (gh == None):
        return 'exists'

    gh.history_add(int(h), int(w), int(t))
    gh.save()

    return 'ok'

