from django.db import models
from django.contrib.gis.db import models
# Create your models here.


class Cities(models.Model):

    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude}) - {self.description}"


class Parks(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.city}({self.latitude}, {self.longitude}) - {self.description}"


class Waterfalls(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.height} {self.city}({self.latitude}, {self.longitude}) - {self.description}"


class Lakes_Reservors(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}  {self.city} ({self.latitude}, {self.longitude}) - {self.description}"


class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude}) - {self.description}"


class Hotels(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude}) - {self.description}"


class Gardens(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.city}({self.latitude}, {self.longitude}) - {self.description}"


class Religious_Places(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.type} {self.city}({self.latitude}, {self.longitude}) - {self.description}"


class MountainPeaks(models.Model):
    name = models.CharField(max_length=100)
    elevation = models.FloatField()
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.elevation} {self.city} ({self.latitude}, {self.longitude}) - {self.description}"


class CampingSites(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.city}({self.latitude}, {self.longitude}) - {self.description}"


class Farms(models.Model):
    name = models.CharField(max_length=100)
    farmType = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.farmType} {self.city}({self.latitude}, {self.longitude}) - {self.description}"


class ConservationForests(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.city}({self.latitude}, {self.longitude}) - {self.description}"


class Factories(models.Model):
    name = models.CharField(max_length=100)
    typeofFactory = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}{self.typeofFactory} {self.city}({self.latitude}, {self.longitude}) - {self.description}"


class NationalParks(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.city}({self.latitude}, {self.longitude}) - {self.description}"


class BestTouristAttractions(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.city}({self.latitude}, {self.longitude}) - {self.description}"


class HikingAreas(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.city}({self.latitude}, {self.longitude}) - {self.description}"
