from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Hospital
from .serializers import HospitalSerializer

# Create your views here.
class HospitalViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Hospital.objects.all()
        serializer = HospitalSerializer(data=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
