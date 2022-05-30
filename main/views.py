import sys

from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied

from users.utilities import check_token
from users.serializers import UserSerializer

from .models import ApplicationModel

from .serializer import ApplicationSerializer

# CONFIGS
settings.SECRET
settings.ALGORITHM


def home(request):
    return HttpResponse(
        """<h3>API is working 😁</h3>
        <p>You can download  the project and run it locally 👋</p>
        <a href="https://github.com/AsqaraliyevFakhriyor/business_traini_api/">API Docs and Source code</a>"""
        )


@api_view(['GET', ])
def application_list(request):
    """Endpoint to get list of all applications"""

    applications = ApplicationModel.objects.all()
    serializer = ApplicationSerializer(
        applications, many=True, context={"request": request})

    payload = check_token(settings.SECRET, settings.ALGORITHM, request)

    user = User.objects.filter(id=payload['id']).first()
    if not user.is_staff:
        raise PermissionDenied("Permission needed")

    userserializer = UserSerializer(user)

    return Response(
        {
            "status_code": status.HTTP_200_OK,
            "applications": serializer.data,
            "user": userserializer.data,
        }
    )


@api_view(["POST", ])
def application_create(request):
    """Endpoint to create new applications and store to database"""

    serializer = ApplicationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        {
            "status_code": status.HTTP_200_OK,
            "application": serializer.data,
        }
    )


@api_view(["DELETE", ])
def application_delete(request):
    """Endpoint to delete specific application"""

    payload = check_token(settings.SECRET, settings.ALGORITHM, request)
    user = User.objects.filter(id=payload['id']).first()

    if not user.is_staff:
        raise PermissionDenied("Permission needed")

    application_id = request.data['application_id']
    try:
        ApplicationModel.objects.get(id=application_id).delete()

        return Response(
            {
                "status_code": status.HTTP_200_OK,
                "application_id": application_id,
            }
        )

    except Exception as e:
        print(sys.exc_info())
        print("e: ", e)
