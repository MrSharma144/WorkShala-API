from django.shortcuts import render

from rest_framework import generics
from .models import InternPreference
from .serializers import InternPreferenceSerializer

class InternPreferenceListCreateAPIView(generics.ListCreateAPIView):
    queryset = InternPreference.objects.all()
    serializer_class = InternPreferenceSerializer

class InternPreferenceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InternPreference.objects.all()
    serializer_class = InternPreferenceSerializer