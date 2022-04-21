from django.contrib import admin
from .models import Location, SavedLocations

# Register your models here.
admin.site.register(Location)
admin.site.register(SavedLocations)
