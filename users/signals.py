from django.db.models.signals import post_save
from django.contrib.auth.models import User#sender
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User) #when user is saved, send this signal
def create_profile(sender,instance,created, **kwargs): #reciever is create profile function
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


