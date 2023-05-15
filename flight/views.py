from rest_framework.viewsets import ModelViewSet
from .models import Flight
from .serializers import FlightSerializer


class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
