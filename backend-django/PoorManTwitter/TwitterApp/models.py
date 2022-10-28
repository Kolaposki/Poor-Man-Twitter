from enum import unique
from pyexpat import model
from django.db import models
import uuid

# Create your models here.


class TwitterApp(models.Model):
    name = models.CharField(max_length=300)
    tweet = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add= True)
    # id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    
    def __str__(self):
        return self.name