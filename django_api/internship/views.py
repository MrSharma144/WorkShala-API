from django.shortcuts import render

# Create your views here
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from .models import Internship,ApplyIntern
from .serializers import InternshipSerializer,InternshipApplicationSerializer


class InternshipListCreateView(generics.ListCreateAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class InternshipDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer


class InternshipApplicationListCreateView(generics.ListCreateAPIView):
    queryset = ApplyIntern.objects.all()
    serializer_class = InternshipApplicationSerializer


# class ResumeUploadView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = uploadSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
