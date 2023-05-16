from rest_framework import routers
from django.urls import path, include
from . import views


app_name = "flight"

router = routers.DefaultRouter()

router.register("flights", views.FlightViewSet, basename="flights")
router.register("airports", views.AirportViewSet, basename="airports")

urlpatterns = [
    path("", include(router.urls)),
]
