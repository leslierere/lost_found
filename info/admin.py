from django.contrib import admin
from .models import LostItem, FoundItem, Site, User

# Register your models here.
admin.site.register(LostItem)
admin.site.register(FoundItem)
admin.site.register(Site)
admin.site.register(User)