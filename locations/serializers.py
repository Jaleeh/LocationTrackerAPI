from django.contrib.auth import models
from rest_framework import fields, serializers
from locations.models import Location, SavedLocations
from useraccounts.models import User

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ( 'lat', 'lng','time','MAC',)
# 'name', 
class CreateLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class SavedLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedLocations
        fields = '__all__'