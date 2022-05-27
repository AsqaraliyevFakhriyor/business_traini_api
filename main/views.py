from multiprocessing import AuthenticationError
import jwt

from .models import ApplicationModel

from django.conf import settings
from django.contrib.auth.models import User

from users.serializers import UserSerializer

from .serializer import ApplicationSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN


ENV = settings.ENV

@api_view()
def application_list(request):
    applications = ApplicationModel.objects.all()
    serializer = ApplicationSerializer(applications, many=True, context= {"request": request})

    token = request.COOKIES.get("token")

    if not token:
        raise AuthenticationFailed("unauthenticated")

    try:
        payload = jwt.decode(token, ENV.str("SECRET"), algorithms=[ ENV.str("ALGORITHM")])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("token expired")
    finally:
        user = User.objects.filter(id=payload['id']).first()
        if not user.is_staff:
            raise PermissionDenied("Permission needed")
            
        userserializer = UserSerializer(user)

    return Response(
        {
        "status_code": 200,
        "success": True,
        "applications": serializer.data,
        "user": userserializer.data,
        },
        HTTP_200_OK
    )
