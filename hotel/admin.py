from django.contrib import admin

from hotel.models import Hotel, Apartment, ApartmentInfo


# Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'city', 'street', 'house_number', 'description', 'rating')
    list_filter = ('rating', 'name', 'country', 'city')
    search_fields = ('name', 'rating', 'city')
    sortable_by = ('price', 'rating', 'name', 'country', 'city')


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'numer_of_beds',)


@admin.register(ApartmentInfo)
class ApartmentInfoAdmin(admin.ModelAdmin):
    list_display = ('apartment_id', 'total_area', 'number_of_bathroom', 'price')
    list_filter = ('total_area', 'price')
    search_fields = ['price']
    sortable_by = ('price', 'total_area')