from django_filters import rest_framework as django_filters

from hotel_rest.models import HotelRest, ApartmentInfoRest


class HotelFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = HotelRest
        fields = ('name', 'country', 'city')


class ApartmentInfoFilter(django_filters.FilterSet):
    numer_of_beds = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.RangeFilter()
    hotel = django_filters.ModelMultipleChoiceFilter(
        queryset=HotelRest.objects.all(),
        field_name='hotel',
        to_field_name='id',
        lookup_expr='exact'
    )

    total_area_and_number_of_bathroom = django_filters.CharFilter(method='filter_by_total_area_and_number_of_bathroom')

    class Meta:
        model = ApartmentInfoRest
        fields = ('numer_of_beds', 'price')

    def filter_by_total_area_and_number_of_bathroom(self, queryset, name, value):
        parts = value.split(',')
        total_area = parts[0]
        number_of_bathroom = parts[1]

        if total_area:
            queryset = queryset.filter(total_area__icontains=total_area)
        if number_of_bathroom:
            queryset = queryset.filter(number_of_bathroom=number_of_bathroom)

        return queryset
