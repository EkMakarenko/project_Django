
from rest_framework import status, generics, mixins, viewsets, serializers

from hotel_rest.models import ApartmentInfoRest, HotelRest


class HotelListSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelRest
        fields = ('name', 'rating', 'country', 'city', 'street', 'house_number', 'image_hotel', )


class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRest
        fields = ('name', 'rating', 'country', 'city', 'street', 'house_number',  'image_hotel',)


class HotelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRest
        fields = ('name', 'rating', 'country', 'city', 'street', 'house_number',)


class HotelImageUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelRest
        fields = ('image_hotel', )


class HotelRecentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRest
        fields = ('name', 'rating', 'country', 'city', 'street', 'house_number', 'image_hotel',)


class HotelRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRest
        fields = '__all__'


class ApartmentInfoListSerializer(serializers.ModelSerializer):
    hotel_in = serializers.SerializerMethodField()

    class Meta:
        model = ApartmentInfoRest
        fields = ('hotel_in', 'total_area', 'number_of_bathroom', 'price', 'image_apartment',)

    def get_hotel_in(self, obj):
        return obj.hotel.full_name


class ApartmentInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentInfoRest
        fields = ('hotel', 'total_area', 'number_of_bathroom', 'price', 'image_apartment',)


class ApartmentInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentInfoRest
        fields = ('hotel', 'total_area', 'number_of_bathroom', 'price',)


class ApartmentInfoImageUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApartmentInfoRest
        fields = ('image_apartment', )


class ApartmentInfoRecentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentInfoRest
        fields = ('total_area', 'number_of_bathroom', 'price',)


class ApartmentInfoRetrieveSerializer(serializers.ModelSerializer):
    hotel = HotelListSerializer()

    class Meta:
        model = HotelRest
        fields = '__all__'
        extra_kwargs = {
            'hotel': {'write_only': True},
        }
