from django.contrib.gis.db import models
from django.utils import timezone

from core.models import BaseModel


class District(BaseModel):
    name = models.CharField(max_length=255)


class House(BaseModel):
    location = models.PointField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)


class Path(BaseModel):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    init_time = models.TimeField()
    weekday = models.PositiveSmallIntegerField()
    polygon = models.LineStringField(null=True)


class Truck(BaseModel):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    number_plate = models.CharField(max_length=10)
    paths = models.ManyToManyField("Path", blank=True)


class Driver(BaseModel):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    driver_license = models.CharField(max_length=12, unique=True)


class Journey(BaseModel):
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE)
    truck = models.ForeignKey("Truck", on_delete=models.CASCADE)
    start_at = models.DateTimeField(default=timezone.now)
    end_at = models.DateTimeField(blank=True, null=True)
