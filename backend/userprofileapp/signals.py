from django.db.models.signals import post_save
from django.dispatch import receiver

from userprofileapp.models import UserProfile
from usersapp.models import MainUser


@receiver(post_save, sender=MainUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)