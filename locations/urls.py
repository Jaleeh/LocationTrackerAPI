from django.urls.conf import path
from locations.views import LocationsAPIView, CreateLocationsAPIView, SavedLocationsAPIView
from . import views

urlpatterns = [
    path('locations/', views.LocationsAPIView.as_view() , name = "locations"),
    path('create_locations/', views.CreateLocationsAPIView.as_view() , name = "create"),
     path('save_location/', views.SavedLocationsAPIView.as_view() , name = "save_location"),
]
# <str:email>/