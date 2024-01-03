from django.contrib import admin

from hotel_rest.models import HotelRest, ApartmentInfoRest


# Register your models here.


@admin.register(ApartmentInfoRest)
class ApartmentInfoRestAdmin(admin.ModelAdmin):
    list_display = ('id', 'numer_of_beds', 'total_area', 'number_of_bathroom', 'price', 'is_available')
    list_filter = ('numer_of_beds', 'total_area', 'number_of_bathroom', 'price',)
    search_fields = ('numer_of_beds',)
    sortable_by = ('price', 'total_area')


@admin.register(HotelRest)
class HotelAdminRest(admin.ModelAdmin):
    list_display = (
        'id',
        'country',
        'name',
        'rating',
        'city',
        'street',
        'house_number',
    )
    list_filter = ('country', 'city')
    search_fields = ('country', 'city', 'name', 'rating', )
    ordering = ('country', 'rating')
