from rest_framework.viewsets import ModelViewSet
from .models import Airport, Flight, Passenger
from .serializers import AirportSerializer, FlightSerializer, PassengerSerializer


class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(ModelViewSet):
    serializer_class = PassengerSerializer

    def get_queryset(self):
        return Passenger.objects.filter(id=self.kwargs.get("flight_pk"))
