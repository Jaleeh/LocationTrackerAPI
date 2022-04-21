from django.db import models
from django.db.models.fields.related import ManyToManyField
from useraccounts.models import User

# Create your models here.
class Location(models.Model):
  #  user== dict of locations{mac address }
  name = models.ForeignKey(User, related_name="person", on_delete=models.CASCADE)
  lat = models.FloatField()
  lng = models.FloatField()
  MAC = models.TextField()
  time = models.DateTimeField(auto_now_add=True)
  # saved = models.BooleanField()
  

class SavedLocations(models.Model):
  name = models.ForeignKey(User, related_name="creator", on_delete=models.CASCADE)
  lat = models.FloatField()
  lng = models.FloatField()
  MAC = models.TextField()
  time = models.DateTimeField(auto_now_add=True)