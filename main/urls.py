from django.urls import path

from .views import application_list

urlpatterns = [
    path("applications", application_list, name="application_list"),
]