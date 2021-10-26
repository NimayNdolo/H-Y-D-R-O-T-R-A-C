from django.shortcuts import render
from rest_framework import generics
from .serializers import LogSerializer
from .models import Log

class LogView(generics.CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer