from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Hospital
from .serializers import HospitalSerializer

# Create your views here.
class HospitalViewSet(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()

