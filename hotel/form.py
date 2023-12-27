from django import forms

from hotel.models import Hotel


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'country', 'city', 'street', 'house_number', 'description', 'rating')