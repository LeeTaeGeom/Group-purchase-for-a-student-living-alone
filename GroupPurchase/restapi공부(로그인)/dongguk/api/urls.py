# api/urls.py
from django.urls import path, include
from .views import HelloAPI, RegistrationAPI, LoginAPI, UserAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("auth/signUP/", RegistrationAPI.as_view()),
    path("auth/signIN/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
]