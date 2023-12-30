from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class ApartmentRest(models.Model):
    numer_of_beds = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.numer_of_beds


class ApartmentInfoRest(models.Model):
    total_area = models.PositiveIntegerField(name=False)
    number_of_bathroom = models.PositiveIntegerField(name=False,validators=[MinValueValidator(1.), MaxValueValidator(10.)])
    price = models.PositiveIntegerField(name=False)
    apartment = models.ForeignKey(ApartmentRest, related_name='apartment', on_delete=models.CASCADE)


class HotelRest(models.Model):
    name = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    street = models.CharField(max_length=50, null=False)
    house_number = models.CharField(max_length=20, null=False)
    rating = models.FloatField(name=False, validators=[MinValueValidator(1.), MaxValueValidator(10.)])
