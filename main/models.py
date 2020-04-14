from django.db import models


class ShopCoordinates(models.Model):
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    address = models.CharField(max_length=240)