from django.contrib import admin
from .models import UserProfile,Location,Inventory

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Location)

admin.site.register(Inventory)
