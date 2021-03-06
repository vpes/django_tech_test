# coding: utf8
from django.db import models

from apps.lines.models import RouteModel
from .locations import LocationModel
from apps.utils import create_id


class StationModel(models.Model):
    """ Station object is the instance of a physical station to be included in a route

        Fields:
            id -- This is the unique identifier for object instance.
            location -- Foreign key to a physical station.
            order --  Position in the route as Integer
            is_active -- the station is active
    """
    class Meta:
        ordering = ['route_id','-is_active','order']
        verbose_name = 'station'
        verbose_name_plural = 'stations'

    id = models.CharField(default=create_id('sta_'), primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(LocationModel, on_delete=models.CASCADE)
    route = models.ForeignKey(RouteModel, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

