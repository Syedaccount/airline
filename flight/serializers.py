from rest_framework import serializers
from .models import *


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["city", "code"]
        model = Airport


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["origin", "destination", "duration", "passengers"]
        model = Flight


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["first_name", "last_name"]
        model = Passenger
