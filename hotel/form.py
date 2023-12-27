from django import forms

from hotel.models import Hotel, Apartment


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'country', 'city', 'street', 'house_number', 'description', 'rating', 'apartment', 'photo')

        apartment = forms.ModelMultipleChoiceField(
            queryset=Apartment.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )
