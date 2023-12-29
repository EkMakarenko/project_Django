from rest_framework import serializers

from hotel_rest import models
from hotel_rest.models import ApartmentInfoRest, HotelRest, ApartmentRest


class ApartmentRestSerializer(serializers.Serializer):
    numer_of_beds = serializers.CharField()

    def create(self, validated_data):
        return ApartmentRest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.numer_of_beds = validated_data.get('numer_of_beds', instance.numer_of_beds)
        instance.save()
        return instance


class ApartmentInfoRestSerializer(serializers.Serializer):
    # apartment_id = models.ForeignKey(ApartmentRest, on_delete=models.CASCADE)
    total_area = serializers.IntegerField()
    number_of_bathroom = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return ApartmentInfoRest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.total_area = validated_data.get('total_area', instance.total_area)
        instance.number_of_bathroom = validated_data.get('number_of_bathroom', instance.number_of_bathroom)
        instance. price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class HotelRestSerializer(serializers.Serializer):
    name = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    street = serializers.CharField()
    house_number = serializers.CharField()
    # photo_country = serializers.ImageField()
    # photo = serializers.ImageField()
    rating = serializers.FloatField()

    def create(self, validated_data):
        return HotelRest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('street', instance.street)
        instance.house_number = validated_data.get('house_number', instance.house_number)
        # instance.photo_country = validated_data.get('photo_country', instance.photo_country)
        # instance.photo = validated_data.get('photo', instance.photo)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance
