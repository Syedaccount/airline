from rest_framework.viewsets import ModelViewSet
from .models import Flight, Airport
from .serializers import FlightSerializer, AirportSerializer


class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
