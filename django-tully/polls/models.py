from django.db import models

class Data(models.Model):
    speed = models.IntegerField()
    acceleration = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='polls')
