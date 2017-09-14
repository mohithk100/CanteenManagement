from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key = True)
    mobileNumber = models.IntegerField(default=0)
    isFaculty = models.BooleanField(default = False)
    avatar= models.ImageField(upload_to = 'User/' , default = '/static/User/defaultProfileImage.png')


def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_user_profile, sender=User)