from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, UpdateUserView
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "user"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("me/", UserDetailView.as_view(), name="user-detail"),
    path("update/", UpdateUserView.as_view(), name="update-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
