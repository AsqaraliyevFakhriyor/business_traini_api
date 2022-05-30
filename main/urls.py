from django.urls import path

from .views import application_list, application_create, application_delete, application_contacted

urlpatterns = [
    path("applications", application_list, name="application_list"),
    path("create/application", application_create, name="application_create"),
    path("delete/application", application_delete, name="application_delete"),
    path("contacted/application", application_contacted, name="application_contacted")
]
