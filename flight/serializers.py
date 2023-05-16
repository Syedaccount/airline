from rest_framework import serializers
from .models import *


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["origin", "destination", "duration"]
        model = Flight


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["city", "code"]
        model = Airport
