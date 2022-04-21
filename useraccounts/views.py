from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from useraccounts.serializers import CustomRegisterSerializer, CustomLoginSerializer, UserListSerializer
# from rest_framework.response import Response
from rest_framework import response, serializers, status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.hashers import make_password



class RegisterAPIView(GenericAPIView):
    serializer_class = CustomRegisterSerializer 

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            password = make_password(self.request.data['password'])
            serializer.save(password=password)

            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(GenericAPIView):
    serializer_class = CustomLoginSerializer


    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        clear = {}
        loca = []
        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            token = Token.objects.get(user=user).key 
            clear['email'] = user.email
            clear['name'] = user.name
            clear['token'] = token
            return response.Response(clear, status=status.HTTP_200_OK)
            # return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()