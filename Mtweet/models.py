from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Meep(models.Model):
    user = models.ForeignKey(
        User, related_name="meeps",
        on_delete=models.DO_NOTHING   
        )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes= models.ManyToManyField(User, related_name="meep_like", blank=True)


    def number_of_likes(self):
         return self.likes.count()
    
    def __str__(self):
         return (
              f"{self.user}"
              f"({self.created_at: %Y-%m-%d  %H : %M }: "
              f"{self.body}...."
               )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",related_name="followed_by",symmetrical=False,blank = True)
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image= models.ImageField(null=True, blank=True, upload_to="images/")

    
    profile_bio = models.CharField(null=True, blank=True,max_length=500)
    homepage_link = models.CharField(null=True, blank=True,max_length=100)
    facebook_link= models.CharField(null=True, blank=True,max_length=100)
    instagram_link= models.CharField(null=True, blank=True,max_length=100)
    linkedin_link= models.CharField(null=True, blank=True,max_length=100)

    
    def __str__(self):
        return self.user.username
    
#@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile = Profile(user=instance)
            user_profile.save()
            user_profile.follows.set([instance.profile.id])
            user_profile.save()
    
post_save.connect(create_profile, sender= User)


from django.conf import settings
from django.db import models

class Follow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers")
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following")
