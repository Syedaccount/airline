from django.db import models


class Airport(models.Model):
    city = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city} ({self.code})"
