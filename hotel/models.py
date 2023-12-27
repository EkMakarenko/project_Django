from django.db import models

# Create your models here.

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Apartment(models.Model):
    numer_of_beds = models.PositiveIntegerField(name=False, validators=[MinValueValidator(1.), MaxValueValidator(10.)])

    # hotel = models.ManyToManyField(Hotel, through="HotelApartment")

    def __int__(self):
        return self.numer_of_beds


class Hotel(models.Model):
    name = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    street = models.CharField(max_length=50, null=False)
    house_number = models.CharField(max_length=20, null=False)
    description = models.TextField()

    rating = models.FloatField(name=False, validators=[MinValueValidator(1.), MaxValueValidator(10.)])
    is_deleted = models.BooleanField(null=False, default=False)

    apartment = models.ManyToManyField(Apartment, through='HotelApartment')

    def __str__(self):
        return self.name


class ApartmentInfo(models.Model):
    apartment_id = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    total_area = models.PositiveIntegerField(name=False)
    number_of_bathroom = models.PositiveIntegerField(name=False,validators=[MinValueValidator(1.), MaxValueValidator(10.)])
    price = models.PositiveIntegerField(name=False)
    is_deleted = models.BooleanField(null=False, default=False)


class HotelApartment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
