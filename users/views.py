import sys

import jwt

import datetime

from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


from .serializers import UserSerializer

from .utilities import check_token


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "status_code": status.HTTP_200_OK,
                "user_data": serializer.data,
            }
        )


class LoginView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed(f"user with {username} doesn't exists!")

        if not user.check_password(password):
            raise AuthenticationFailed(f"wrong password for {username}")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, settings.SECRET,
                           algorithm=settings.ALGORITHM)

        response = Response()
        response.set_cookie(key="token", value=token, httponly=True)

        response.data = {
            "status_code": status.HTTP_200_OK,
        }

        return response


class UserDataView(APIView):

    def get(self, request):
        payload = check_token(settings.SECRET, settings.ALGORITHM, request)

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(
            {
                "status_code": status.HTTP_200_OK,
                "user_data": serializer.data,
            }
        )


class LogoutView(APIView):

    def post(self, request):
        response = Response()
        try:
            response.delete_cookie("token")

            response.data = {
                "status_code": status.HTTP_200_OK,
            }

        except Exception as e:
            print(sys.exc_info())
            print(e)
            raise AuthenticationFailed("unauthenticated")

        return response
