from statistics import mode
from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    starring = models.CharField(max_length=300)

    def __str__(self):
        return self.name