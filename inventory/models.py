from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class Authentication(models.Model):
    user=models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    phone=models.CharField(max_length=11)
    password=models.IntegerField()

