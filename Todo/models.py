from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField(default=timezone.now)
    unique_id = models.CharField(unique=True, max_length=255, default='')
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id =  str(uuid.uuid4())
        super().save(*args, **kwargs)
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

    