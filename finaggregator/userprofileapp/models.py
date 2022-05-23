from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from usersapp.models import User


class UserProfile(models.Model):
    objects = models.Manager()

    user            = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='userprofile')
    avatar          = models.ImageField(upload_to='profile/photo', blank=True)
    phone           = PhoneNumberField(blank=True)
    inn_field       = models.IntegerField(null=True, blank=True)
    address         = models.CharField(max_length=512, blank=True)
    first_name      = models.CharField(_("first name"), max_length=150, blank=True)
    middle_name     = models.CharField(_("middle name"), max_length=150, blank=True)
    last_name       = models.CharField(_("last name"), max_length=150, blank=True)