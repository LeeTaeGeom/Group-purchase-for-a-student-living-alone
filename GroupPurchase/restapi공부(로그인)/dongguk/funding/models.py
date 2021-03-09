from django.db import models
import api
# Create your models here.

class Funding(models.Model):
    id = models.UUIDField(primary_key=True,max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    #participants=api
    price=models.IntegerField(max_length=200)
    expect_destination=models.CharField(max_length=200)
    additional=models.CharField(max_length=200)
    isAccepted=models.BooleanField(max_length=200)
    categories=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
