from django.contrib import admin
from django.urls import path
from . import views
from .views import RegisterView,LoginAPIView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name= 'login')
]
