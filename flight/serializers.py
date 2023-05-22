from rest_framework import serializers
from .models import *


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "city", "code"]
        model = Airport


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "user_id", "phone", "birth_date"]
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
        fields = ["passenger"]
        model = BookFlight

    passenger = PassengerSerializer(read_only=True)

    def create(self, validated_data):
        user_id, flight_id = self.context.get("user_id"), self.context.get("flight_id")
        passenger = Passenger.objects.get(user_id=user_id)
        return BookFlight.objects.create(passenger_id=passenger.id, flight_id=flight_id)
