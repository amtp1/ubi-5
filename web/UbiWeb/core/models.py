import re
import uuid
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


class UserProfile(AbstractBaseUser, PermissionsMixin):
    user_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=128, blank=True, null=True)
    last_active = models.DateTimeField(auto_now_add=False, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []


class Attack(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.BigIntegerField()
    phone = models.BigIntegerField(null=True)
    is_run = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
