from django.db import models


class ApartmentManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_available=True, is_deleted=False)


class UnavailableApartmentManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_available=False, is_deleted=False)
