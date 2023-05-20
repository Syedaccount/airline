from rest_framework.viewsets import ModelViewSet
from .models import Airport, Flight, Passenger
from .serializers import AirportSerializer, FlightSerializer, PassengerSerializer, CreateFlightSerializer


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

    def get_queryset(self):
        return Passenger.objects.filter(id=self.kwargs.get("flight_pk"))
