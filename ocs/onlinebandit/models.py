import datetime
from django.db import models
from django.utils import timezone

class user(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    regtime = models.TimeField()
    level = models.SmallIntegerField()

class plan(models.Model):
    owner = models.ForeignKey(user)
    planname = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    state = models.SmallIntegerField()
    time = models.TimeField(default=timezone.now())
    # uploading -> pending -> scanning -> complete

class item(models.Model):
    owner = models.ForeignKey(plan)
    issue = models.CharField(max_length=100)
    severity = models.SmallIntegerField()
    probability = models.SmallIntegerField()
    instruction = models.CharField(max_length=255)
# Create your models here.
