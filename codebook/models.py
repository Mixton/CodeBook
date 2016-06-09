from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
Model = models.Model

class Post(Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField()

class Follow(Model):
    '''
    uid = models.OneToOneField(
            User,
            on_delete=models.CASCADE,
            related_name = "User"
        )

    fid = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name = "Follower"
        )
    '''

    uid = models.IntegerField()
    fid = models.IntegerField()

# Create your models here.
