from django.db import models
from django.util import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    pass

class Group(models.Model):
    group_name = models.CharField(max_length=20)
    create = models.DateTimeField()
    update = models.DateTimeField()
    visible = models.IntegerField()

class Question(models.Model):
    type = models.IntegerField()
    sidea = models.TextField()
    sideb = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group)
    create = models.DateTimeField()
    update = models.DateTimeField()

class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    questioin = models.ForeignKey(Question, on_delete=models.CASCADE)
    last_time_correct = models.BooleanField(default=False)
    continuous_correct = models.IntegerField()
    correct_count = models.IntegerField()
    show_count = models.IntegerField()

class Config(models.Model):
    threshhold = models.IntegerField()

