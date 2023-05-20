from rest_framework_nested import routers
from django.urls import path, include
from . import views


app_name = "flight"

router = routers.DefaultRouter()

router.register("airports", views.AirportViewSet, basename="airports")
router.register("flights", views.FlightViewSet, basename="flights")

flights_router = routers.NestedDefaultRouter(router, "flights", lookup="flight")
flights_router.register("passengers", views.PassengerViewSet, basename="flight_passengers")
flights_router.register("book", views.BookFlightViewSet, basename="flight_book")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(flights_router.urls))
]
