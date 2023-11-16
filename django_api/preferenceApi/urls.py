from django.urls import path
from .views import InternPreferenceListCreateAPIView, InternPreferenceDetailAPIView

urlpatterns = [
    path('preferences/', InternPreferenceListCreateAPIView.as_view(), name='preferences-list'),
    path('preferences/<int:pk>/', InternPreferenceDetailAPIView.as_view(), name='preferences-detail'),
]