import random
import string
from django.shortcuts import render

from .models import User
from .serializers import RegisterSerializer
from .serializers import LoginSerializer
from rest_framework import generics
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework import views
from . import serializers
from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.authtoken.models import Token


# Create your views here.

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        #Check login is successful or not
        token, _ = Token.objects.get_or_create(user=user)
        # print(token)
        # return Response(None, status=status.HTTP_200_OK) 
        return JsonResponse({'Auth_Token': token.key}, status=status.HTTP_200_OK)