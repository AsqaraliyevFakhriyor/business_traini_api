from django.urls import path

from .views import RegisterView, LoginView, UserDataView, LogoutView

app_name = "user"

urlpatterns = [
    path('register', RegisterView.as_view(), name="user_login"),
    path("login", LoginView.as_view(), name="user_login"),
    path("user_data", UserDataView.as_view(), name="user_info"),
    path('logout', LogoutView.as_view(), name = "user_logout")
]