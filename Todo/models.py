from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User

# Create your models here.

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

    