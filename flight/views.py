from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Airport, Flight, Passenger, BookFlight
from .serializers import (AirportSerializer, FlightSerializer,
                          PassengerSerializer, CreateFlightSerializer,
                          BookFlightSerializer)


class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateFlightSerializer
        return FlightSerializer


class PassengerViewSet(ModelViewSet):
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Passenger.objects.filter(id=self.kwargs.get("flight_pk"))


class BookFlightViewSet(ModelViewSet):
    queryset = BookFlight.objects.all()
    serializer_class = BookFlightSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        print(self.kwargs)
        return {"user_id": self.request.user.id, "flight_id": self.kwargs.get("flight_pk")}
