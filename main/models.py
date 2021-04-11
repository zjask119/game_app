from django.db import models


class Character(models.Model):
    id = models.Field
    name = models.CharField(max_length=40)
    race = models.CharField(max_length=30, default='Earthling')
    height = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    recovery = models.IntegerField(default=0)
    nature = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    movement = models.IntegerField(default=0)
    sense = models.IntegerField(default=0)
    solar = models.IntegerField(default=0)
    path = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Move (models.Model):
    id = models.Field
    name = models.CharField(max_length=40)
    power = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    sacrifice = models.IntegerField(default=0)
    type = models.CharField(max_length=40)
    rage = models.CharField(max_length=40)
    user = models.CharField(max_length=40)

    def __str__(self):
        return self.name
