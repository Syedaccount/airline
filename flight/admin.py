from django.contrib import admin
from django.db.models import Count
from django.utils.html import urlencode, format_html
from django.urls import reverse
from .models import Airport, Flight, Passenger, BookFlight


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ["city", "code", "is_open"]
    search_fields = ["city"]
    list_editable = ["is_open"]


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    autocomplete_fields = ["origin", "destination"]
    list_display = ["origin", "destination", "date_time",
                    "passengers_count", "duration", "total_seat",
                    "remaining_seat"]
    list_filter = ["origin", "destination"]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            passengers_count=Count("passengers")
        )

    @admin.display(ordering="passengers_count")
    def passengers_count(self, flight: Flight):
        url = (
                reverse("admin:flight_passenger_changelist")
                + "?"
                + urlencode({
                    "flight__id": str(flight.id)
                }))
        return format_html('<a href="{}">{}</a>', url, flight.passengers_count)


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


@admin.register(BookFlight)
class BookFlightAdmin(admin.ModelAdmin):
    list_display = ["flight"]