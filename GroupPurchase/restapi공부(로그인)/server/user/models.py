from django.db import models

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True,max_length=200)
    user_id = models.CharField(max_length=200)
    user_pw = models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    isAccepted=models.BooleanField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True) 
    
