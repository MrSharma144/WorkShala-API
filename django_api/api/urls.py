from django.contrib import admin
from django.urls import path
from . import views

from .views import RegisterView,LoginAPIView,VerifyEmail,ProfileListCreateAPIView,ProfileDetailAPIView




urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('login/',LoginAPIView.as_view(),name= 'login'),
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<str:user__username>/', ProfileDetailAPIView.as_view(), name='profile-detail'),
]
