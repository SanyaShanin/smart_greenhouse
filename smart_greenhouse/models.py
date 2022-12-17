from django.db import models
import hashlib
import uuid
import datetime

def history_default():
    return []

def make_uuid():
    return uuid.uuid4().hex[:5] + "!" + str(Greenhouse.objects.count())

def status_ok():
    return 'ok'

def status_user():
    return 'user'

class Greenhouse(models.Model):
    identificator = models.CharField(max_length=40, default=make_uuid)

    light = models.BooleanField()
    water = models.BooleanField()
    wind = models.BooleanField()
    history = models.JSONField(default=history_default)
    status = models.CharField(max_length=80, default=status_ok)

    def history_add(self, h, w, t):
        if (len(self.history)) > 336:
            del self.history[0]
        self.history.append([datetime.datetime.utcnow().timestamp(), h, w, t])

    def get(self):
        return {
            'id': self.identificator,
            'light': self.light,
            'water': self.water,
            'wind': self.wind,
            'history': self.history
            }

    def get_state(self):
        return {
            'light': self.light,
            'water': self.water,
            'wind': self.wind
            }

class User(models.Model):
    password = models.CharField(max_length=40)
    mail = models.CharField(max_length=80)
    login = models.CharField(max_length=40)
    name = models.CharField(max_length=80)
    status = models.CharField(max_length=10, default=status_user)
    greenhouses = models.ManyToManyField(Greenhouse)

    def validate_password(self, password):
        return self.password == hashlib.md5(password.encode('utf-8')).hexdigest();

    def set_password(self, password):
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest();

    def set_name(self, name):
        self.name = name;

    def set_login(self, login):
        self.login = login;

    def gh_clear(self):
        self.greenhouses = "";

    def gh_get(self):
        return [gh.identificator for gh in self.greenhouses.all()]

    def gh_add(self, gh):
        self.greenhouses.add(gh)

    def get(self):
        return {
            'name': self.name,
            'login': self.login,
            'mail': self.mail,
            'status': self.status,
            'greenhouses': self.gh_get()
            }

    def sessions(self):
        return Session.all().values_list('identificator', flat=True)

class Session(models.Model):
    login = models.CharField(max_length=40)
    identificator = models.CharField(max_length=40, default=make_uuid)

    def user(self):
        return User.objects.get(login=self.login)


