from django.db import models
from datetime import date

# Create your models here.

class Car(models.Model):
    image= models.ImageField()
    make = models.DateField(default=date(2024, 9, 27))
    model = models.CharField(max_length=100)
    mileage = models.IntegerField()
    engine_capacity = models.IntegerField()
    fuel_type = models.CharField(max_length=1000)
