from authentication import views
from django.urls import path

urlpatterns = [
    path("register", views.RegisterAPIView.as_view(), name="register"),
    path("login", views.LoginApiView.as_view(), name="login"),
]