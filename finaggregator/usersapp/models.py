from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class User(AbstractUser):
    id              = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    username        = models.CharField(max_length=64, unique=True)
    email           = models.EmailField(max_length=256, blank=False, unique=True)
    first_name      = None
    last_name       = None


# class User2(AbstractUser):
#     id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
#     username = models.CharField(max_length=64, unique=True)
#     middle_name = models.CharField(_("middle name"), max_length=150, blank=True)
#     email = models.EmailField(max_length=256, blank=False, unique=True)
#     avatar = models.ImageField(upload_to='profile/photo', blank=True)
#     phone = PhoneNumberField(blank=True)
#     inn_field = models.IntegerField(null=True, blank=True)
#     address = models.CharField(max_length=512, blank=True)
