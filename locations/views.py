from rest_framework.settings import perform_import
from rest_framework.views import APIView
from locations.serializers import CreateLocationsSerializer, SavedLocationsSerializer
from locations.serializers import LocationsSerializer
from useraccounts.models import User
from django.shortcuts import render
from django.http.response import Http404
from rest_framework import generics, permissions
# from rest_framework.response import Response
from rest_framework import response, serializers, status
from locations.models import Location, SavedLocations

# Create your views here.
class LocationsAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LocationsSerializer
    def get_queryset(self):
      return Location.objects.filter(name=self.request.user)

class SavedLocationsAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SavedLocationsSerializer
    
    def perform_create(self, serializer):
        serializer.save(name=self.request.user)

    def get_queryset(self):
        return SavedLocations.objects.all()

   

class CreateLocationsAPIView(generics.GenericAPIView):

    serializer_class = CreateLocationsSerializer
    queryset = Location.objects.all()
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
