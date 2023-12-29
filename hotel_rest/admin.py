from django.contrib import admin

from hotel_rest.models import HotelRest, ApartmentInfoRest, ApartmentRest


# Register your models here.


@admin.register(ApartmentRest)
class ApartmentRestAdmin(admin.ModelAdmin):
    list_display = ('id', 'numer_of_beds')
    list_filter = ('numer_of_beds', )
    search_fields = ('numer_of_beds',)


@admin.register(ApartmentInfoRest)
class ApartmentInfoRestAdmin(admin.ModelAdmin):
    list_display = ('total_area', 'number_of_bathroom', 'price',)
    list_filter = ('total_area', 'price')
    search_fields = ['price']
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
