from django.db import models


# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=255)
    animedata = models.FloatField()
    animeseision = models.IntegerField()
    image = models.CharField(max_length=2083)