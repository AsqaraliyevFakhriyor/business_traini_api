from .models import User

from .serializers import UserSerializer

from django.shortcuts import get_list_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


class RegisterView(APIView):
     def post(self, request):
         serializer = UserSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed(f"User with {email} doesn't exists!")

        if not user.check_password(password):
            raise AuthenticationFailed(f"Wrong password for {email}")


        return Response({
            "success": True,
            "user": user.name,
            "status_code": 200,
            "user": user.name,
            }, 200)
