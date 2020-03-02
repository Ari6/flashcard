from django.db import models
from django.util import timezone

class Question(models.Model):
    type = models.IntegerField()
    sidea = models.TextField()
    sideb = models.TextField()
    user = models.ForeignKey(on_delete=models.CASCADE)
    group = models.ForeignKey(Group)
    create = models.DateTimeField()
    update = models.DateTimeField()

class Group(models.Model):
    g_name = models.CharField(max_length=20)
    create = models.DateTimeField()
    update = models.DateTimeField()
    visible = models.IntegerField()