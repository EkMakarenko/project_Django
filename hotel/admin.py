from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from hotel.models import Hotel, Apartment, ApartmentInfo, HotelApartment


# Register your models here.


class HotelApartmentInline(admin.StackedInline):
    model = HotelApartment
    extra = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'display_photo_country',
        'country',
        'name',
        'rating',
        'display_apartment',
        'city',
        'street',
        'house_number',
        'custom_field',
    )
    list_filter = ('country', 'city')
    search_fields = ('country', 'city', 'name', 'rating', )
    ordering = ('country', 'rating')
    inlines = (HotelApartmentInline, )
    fieldsets = (
        ('Main Information', {
            'fields': ('name', 'rating', 'description'),
        }),
        ('Address', {
            'fields': ('country', 'city', 'street', 'house_number',),
        }),
        ('Photo', {
            'fields': ('photo', 'photo_country'),
            'classes': ('collapse',),
        })
    )

    def display_photo_country(self, obj):
        return format_html('<img src="{}" height="20"/>', obj.photo_country.url) if obj.photo_country else ''

    def custom_field(self, obj):
        return 'Rating below 6' if obj.rating < 7 else 'OK'

    def display_apartment(self, obj):
        apartments = obj.apartment.all()
        href = '<a href="{}">{}</a>'
        url = 'admin:hotel_apartment_change'
        links = [format_html(href, reverse(url, args=[apartment.id]), apartment.numer_of_beds) for apartment in apartments]
        return format_html(', '.join(links))

    custom_field.short_description = "Rating Ok"
    display_photo_country.short_description = "Photo"


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'numer_of_beds')
    list_filter = ('numer_of_beds', )
    search_fields = ('numer_of_beds',)


@admin.register(HotelApartment)
class HotelApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'apartment')
    list_filter = ('hotel', 'apartment')
    search_fields = ('hotel', 'apartment')


@admin.register(ApartmentInfo)
class ApartmentInfoAdmin(admin.ModelAdmin):
    list_display = ('apartment_id', 'total_area', 'number_of_bathroom', 'price')
    list_filter = ('total_area', 'price')
    search_fields = ['price']
    sortable_by = ('price', 'total_area')