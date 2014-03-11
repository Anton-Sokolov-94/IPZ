from django.db import models
from django.contrib.auth.models import User
from profiles.fields import AutoOneToOneField


class UserProfile(models.Model):
    user = AutoOneToOneField(User, related_name='UserProfile', verbose_name=('User'), primary_key=True)
    about = models.TextField(blank=True)
    payment_account = models.CharField(max_length=32, blank=True)
    user_type = models.BooleanField()