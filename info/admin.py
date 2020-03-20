from django.contrib import admin
from .models import Item, Site, User

# Register your models here.
admin.site.register(Item)
admin.site.register(Site)
admin.site.register(User)