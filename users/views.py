import os

import sys

import jwt

import datetime

from .models import User

from django.conf import settings
from django.shortcuts import get_list_or_404

from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN


ENV = settings.ENV

class RegisterView(APIView):
     def post(self, request):
         serializer = UserSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(
             {
             "status_code": 200,
             "user_data": serializer.data,
             "description": "Successfully authenticated"
            }, HTTP_200_OK
         )


class LoginView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed(f"User with {email} doesn't exists!")

        if not user.check_password(password):
            raise AuthenticationFailed(f"Wrong password for {email}")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, ENV.str("SECRET"), algorithm=ENV.str("ALGORITHM"))

        response = Response()
        response.set_cookie(key="token", value=token, httponly=True)

        response.data ={
            "status_code": 200,
            "description": "Successfully logged in"
        }, HTTP_200_OK


        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get("token")

        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            payload = jwt.decode(token, ENV.str("SECRET"), algorithms=[ENV.str("ALGORITHM"),])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token Expired")
        finally:
            user = User.objects.filter(id=payload['id']).first()
            serializer = UserSerializer(user)

        return Response(
            {
            "status_code": 200,
            "user_data": serializer.data,
            },
            HTTP_200_OK
        )

class LogOutView(APIView):
    
    def post(self, request):
        response = Response()
        response.delete_cookie("token")
        response.data = {
            "status_code": 200,
            "description": "Successfully loged out"
        }, HTTP_200_OK

        return response