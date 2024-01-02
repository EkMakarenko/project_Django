
from rest_framework import status, generics, mixins, viewsets, serializers

# from hotel_rest.models import ApartmentInfoRest

# from hotel_rest import models
from hotel_rest.models import ApartmentInfoRest, HotelRest

# 1 способ (Apiview)_______________________________

#
# class ApartmentRestSerializer(serializers.Serializer):
#     numer_of_beds = serializers.CharField()
#
#     def create(self, validated_data):
#         return ApartmentRest.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.numer_of_beds = validated_data.get('numer_of_beds', instance.numer_of_beds)
#         instance.save()
#         return instance
#
#
# class ApartmentInfoRestSerializer(serializers.Serializer):
#     apartment_id = serializers.IntegerField()
#     total_area = serializers.IntegerField()
#     number_of_bathroom = serializers.IntegerField()
#     price = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return ApartmentInfoRest.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.apartment_id = validated_data.get('apartment_id', instance.apartment_id)
#         instance.total_area = validated_data.get('total_area', instance.total_area)
#         instance.number_of_bathroom = validated_data.get('number_of_bathroom', instance.number_of_bathroom)
#         instance. price = validated_data.get('price', instance.price)
#         instance.save()
#         return instance
#
#
# class HotelRestSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     country = serializers.CharField()
#     city = serializers.CharField()
#     street = serializers.CharField()
#     house_number = serializers.CharField()
#     # photo_country = serializers.ImageField()
#     # photo = serializers.ImageField()
#     rating = serializers.FloatField()
#
#     def create(self, validated_data):
#         return HotelRest.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.country = validated_data.get('country', instance.country)
#         instance.city = validated_data.get('city', instance.city)
#         instance.street = validated_data.get('street', instance.street)
#         instance.house_number = validated_data.get('house_number', instance.house_number)
#         # instance.photo_country = validated_data.get('photo_country', instance.photo_country)
#         # instance.photo = validated_data.get('photo', instance.photo)
#         instance.rating = validated_data.get('rating', instance.rating)
#         instance.save()
#         return instance
#

# # 2 способ (genericApiview) ________________________________________________
# class ApartmentRestSerializer(serializers.Serializer):
#     class Meta:
#         model = ApartmentRest
#         fields = '__all__'
#
# class ApartmentInfoRestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApartmentInfoRest
#         # fields = '__all__'
#         exclude = ('is_deleted',)
#
# class ApartmentInfoRestSingleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApartmentInfoRest
#         fields = '__all__'
#
# class HotelRestSerializer(serializers.Serializer):
#     class Meta:
#         model = HotelRest
#         fields = '__all__'


# 3 способ (ViewSet)____________________________________

# class ApartmentsRestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApartmentRest
#         fields = '__all__'


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
        fields = ('hotel', 'total_area', 'number_of_bathroom', 'price', 'image_apartment',)


class ApartmentInfoRetrieveSerializer(serializers.ModelSerializer):
    hotel = HotelListSerializer()

    class Meta:
        model = HotelRest
        fields = '__all__'
        extra_kwargs = {
            'hotel': {'write_only': True},
        }
