from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from hotel.models import Hotel


# Create your models here.


class Comment(models.Model):
    """"""

    text = models.TextField(blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1.), MaxValueValidator(10.)])
    created_at = models.DateTimeField(auto_now_add=True)

    info_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comments')
