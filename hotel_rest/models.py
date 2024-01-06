from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from hotel_rest.managers import ApartmentManager, UnavailableApartmentManager


# Create your models here.


class HotelRest(models.Model):
    name = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    street = models.CharField(max_length=50, null=False)
    house_number = models.CharField(max_length=20, null=False)
    rating = models.FloatField(name=False, validators=[MinValueValidator(1.), MaxValueValidator(10.)])
    image_hotel = models.ImageField(upload_to='hotel_rest/', null=True, blank=True)
    is_deleted = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name

    @property
    def full_name(self):
        return f'{self.name}'


class ApartmentInfoRest(models.Model):
    numer_of_beds = models.CharField(max_length=30, null=False)
    total_area = models.PositiveIntegerField(name=False)
    number_of_bathroom = models.PositiveIntegerField(name=False,validators=[MinValueValidator(1.), MaxValueValidator(10.)])
    price = models.PositiveIntegerField(name=False)
    hotel = models.ForeignKey(HotelRest, related_name='hotel', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(null=False, default=False)
    image_apartment = models.ImageField(upload_to='apartment_rest/', null=True, blank=True)
    is_available = models.BooleanField(null=False, default=True)

    objects = models.Manager()
    available_objects = ApartmentManager()
    unavailable_objects = UnavailableApartmentManager()
