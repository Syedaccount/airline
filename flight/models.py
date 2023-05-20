from django.db import models
from django.conf import settings


class Airport(models.Model):

    IS_OPEN_YES = "Yes"
    IS_OPEN_NO = "No"

    IS_OPEN_CHOICES = [
        (IS_OPEN_YES, "Yes"),
        (IS_OPEN_NO, "No")
    ]
    city = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    is_open = models.CharField(max_length=5, choices=IS_OPEN_CHOICES, default=IS_OPEN_YES)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    total_seat = models.PositiveSmallIntegerField()
    remaining_seat = models.PositiveSmallIntegerField()


class Passenger(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flight = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    phone = models.CharField(max_length=64)
    birth_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name


class BookFlight(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="reservations")
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
