from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/users')
    bio = models.TextField(null=True, blank=True, max_length=150, help_text="This is my Bio")
    phone = models.CharField(null=True, blank=True, max_length=11, help_text="Phone Number")
    address = models.CharField(null=True, blank=True, max_length=100, help_text="Address")


    def __str__(self):
        return self.user.username


# create profile when new user signs up

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)
