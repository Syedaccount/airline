from django.contrib import admin
from django.db.models import Count
from django.utils.html import urlencode, format_html
from django.urls import reverse
from .models import Airport, Flight, Passenger


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ["city", "code"]
    search_fields = ["city"]


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    autocomplete_fields = ["origin", "destination"]
    list_display = ["origin", "destination", "date_time", "passengers_count", "duration"]
    list_filter = ["origin", "destination"]

    @admin.display(ordering="passengers_count")
    def passengers_count(self, flight: Flight):
        return flight.passengers.count()

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            passengers_count=Count("passengers")
        )


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "flights_count"]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            flights_count=Count("flight")
        )

    @admin.display(ordering="flights_count")
    def flights_count(self, passenger: Passenger):
        url = (
                reverse("admin:flight_flight_changelist")
                + "?"
                + urlencode({
                     "passengers__id": str(passenger.id)
                }))
        return format_html('<a href="{}">{}</a>', url, passenger.flights_count)

