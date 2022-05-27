from django.urls import path

from .views import RegisterView, LoginView, UserView

app_name = "user"

urlpatterns = [
    path('register', RegisterView.as_view(), name="user_login"),
    path("login", LoginView.as_view(), name="login"),
    path("user", UserView.as_view(), name="user")

]