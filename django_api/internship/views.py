from django.shortcuts import render

# Create your views here.
# internships/views.py
from rest_framework import generics
from .models import Internship
from .serializers import InternshipSerializer

class InternshipListCreateView(generics.ListCreateAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
