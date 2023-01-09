from django.contrib.gis.db import models
from core.models import BaseModel


class District(BaseModel):
    name = models.CharField(max_length=255)


class Truck(BaseModel):
    district = models.ForeignKey(District, on_delete=models.CASCADE)


class House(BaseModel):
    location = models.PointField()


class Path(BaseModel):
    init_time = models.TimeField()
    weekday = models.PositiveSmallIntegerField()
