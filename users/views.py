import sys

import jwt

import datetime


from .serializers import UserSerializer

from django.conf import settings
from django.contrib.auth.models import User

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
             "description": "successfully authenticated"
            }, HTTP_200_OK
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

        token = jwt.encode(payload, ENV.str("SECRET"), algorithm=ENV.str("ALGORITHM"))

        response = Response()
        response.set_cookie(key="token", value=token, httponly=True)

        response.data ={
            "status_code": 200,
            "description": "successfully logged in"
        }, HTTP_200_OK


        return response


class UserDataView(APIView):

    def get(self, request):
        token = request.COOKIES.get("token")

        if not token:
            raise AuthenticationFailed("unauthenticated")

        try:
            payload = jwt.decode(token, ENV.str("SECRET"), algorithms=[ENV.str("ALGORITHM"),])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("token expired")
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

class LogoutView(APIView):

    def post(self, request):
        response = Response()
        try:
            response.delete_cookie("token")
        except Exception as e:
            print(sys.exc_info())
            print(e)
            raise AuthenticationFailed("unauthenticated")
        finally:
            response.data = {
                "status_code": 200,
                "description": "successfully loged out"
            }, HTTP_200_OK

        return response