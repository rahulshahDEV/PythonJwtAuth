from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginUser.as_view()),
    path('userinfo/', UserAPI.as_view()),
    path('logout', UserLogout.as_view()),
    ]