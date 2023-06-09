from .models import Hospital
from rest_framework.response import Response
from rest_framework import serializers

class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = '__all__'

    def validate_latitude(self, value):
        
        if value < -90.0 or value > 90:
            raise serializers.ValidationError('Latitude must be between -90 and 90 degree.')
        return value
    
    def validate_longitude(self, value):
        
        if value < -180.0 or value > 180:
            raise serializers.ValidationError('Longitude must be between -180 and 180 degree.')
        return value
