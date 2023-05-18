from django.db import models


class Airport(models.Model):
    city = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    is_open = models.BooleanField(default=True)

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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    flight = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
