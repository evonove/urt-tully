from django.db import models

class Data(models.Model):
    speed = models.IntegerField()
    acceleration = models.IntegerField()
