from rest_framework import serializers
from .models import *


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "city", "code"]
        model = Airport


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "user_id", "first_name", "last_name"]
        model = Passenger


class CreateFlightSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["origin", "destination", "duration", "total_seat", "remaining_seat"]
        model = Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "origin", "destination", "duration", "passengers", "total_seat", "remaining_seat"]
        model = Flight
    origin = AirportSerializer()
    destination = AirportSerializer()
    passengers = PassengerSerializer(many=True, read_only=True)


class BookFlightSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["flight", "passenger"]
        model = BookFlight

    flight = FlightSerializer(read_only=True)
    passenger = PassengerSerializer(read_only=True, many=True)

    def create(self, validated_data):
        print("create -----------------=============")
        print(self.context)
        print(validated_data)