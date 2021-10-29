from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField, DateTimeField

# Create your models here.
class Location(models.Model):

    name=models.CharField(max_length=50)
    date=DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.name
     
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    phone=models.CharField(max_length=11)

    def __str__(self):
        return self.user.username


        
class Inventory(models.Model):
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    date=DateTimeField(auto_now_add=True)




# class Authentication(models.Model):
#     user=models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
#     phone=models.CharField(max_length=11)
    

