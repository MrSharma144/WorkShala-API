from rest_framework.response import responses
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import RegisterSerlizer
from rest_framework import generics,status






# Create your views here.
class RegisterView(generics.GenericAPIView):
    
    serializer_class = RegisterSerlizer
    

    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data,status=status.HTTP_201_CREATED)