from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from hotel.models import ApartmentInfo
from hotel_rest.models import ApartmentRest, ApartmentInfoRest, HotelRest
from hotel_rest.serializers import ApartmentRestSerializer, ApartmentInfoRestSerializer, HotelRestSerializer


# Create your views here.

class ApartmentCreateReadView(APIView):
    def get(self, request):
        apartment_rest = ApartmentRest.objects.all()
        serializer = ApartmentRestSerializer(apartment_rest, many=True)
        return Response({'apartment_rest': serializer.data})

    def post(self, request):
        apartment_rest = request.data.get('apartment_rest')
        serializer = ApartmentRestSerializer(data=apartment_rest)
        if serializer.is_valid(raise_exception=True):
            new_apartment_rest = serializer.save()
        list_serializer = ApartmentRestSerializer(new_apartment_rest)
        return Response({'new_apartment_rest': list_serializer.data})


class ApartmentUpdateDeleteView(APIView):
    def get(self, request, pk):
        apartment= ApartmentInfoRest.objects.get(id=pk)
        serializer = ApartmentRestSerializer(apartment)
        return Response({'apartment': serializer.data})

    def put(self, request, pk):
        apartment = get_object_or_404(ApartmentRest.objects.all(), pk=pk)
        data = request.data.get('apartment')
        serializer = ApartmentRestSerializer(data=data, instance=apartment, partial=True)
        if serializer.is_valid(raise_exception=True):
            new_apartment = serializer.save()
        list_serializer = ApartmentRestSerializer(new_apartment)
        return Response({'update_apartment': list_serializer.data})

    def delete(self, request, pk):
        apartment = get_object_or_404(ApartmentRest.objects.all(), pk=pk)
        apartment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApartmentInfoCreateReadView(APIView):
    def get(self, request):
        apartment_info = ApartmentInfoRest.objects.all()
        serializer = ApartmentInfoRestSerializer(apartment_info, many=True)
        return Response({'apartment_info': serializer.data})

    def post(self, request):
        apartment_info = request.data.get('apartment_info')
        serializer = ApartmentInfoRestSerializer(data=apartment_info)
        if serializer.is_valid(raise_exception=True):
            new_apartment_info = serializer.save()
        list_serializer = ApartmentInfoRestSerializer(new_apartment_info)
        return Response({'new_apartment_info': list_serializer.data})


class ApartmentInfoUpdateDeleteView(APIView):
    def get(self, request, pk):
        apartment_info = ApartmentInfoRest.objects.get(id=pk)
        serializer = ApartmentInfoRestSerializer(apartment_info)
        return Response({'apartment_info': serializer.data})

    def put(self, request, pk):
        apartment_info = get_object_or_404(ApartmentInfoRest.objects.all(), pk=pk)
        data = request.data.get('apartment_info')
        serializer = ApartmentInfoRestSerializer(data=data, instance=apartment_info, partial=True)
        if serializer.is_valid(raise_exception=True):
            new_apartment_info = serializer.save()
        list_serializer = ApartmentInfoRestSerializer(new_apartment_info)
        return Response({'update_apartment_info': list_serializer.data})

    def delete(self, request, pk):
        apartment_info = get_object_or_404(ApartmentInfoRest.objects.all(), pk=pk)
        apartment_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HotelCreateReadView(APIView):
    def get(self, request):
        hotel = HotelRest.objects.all()
        serializer = HotelRestSerializer(hotel, many=True)
        return Response({'hotel': serializer.data})

    def post(self, request):
        hotel = request.data.get('hotel')
        serializer = HotelRestSerializer(data=hotel)
        if serializer.is_valid(raise_exception=True):
            new_hotel = serializer.save()
        list_serializer = HotelRestSerializer(new_hotel)
        return Response({'new_hotel': list_serializer.data})

class HotelUpdateDeleteView(APIView):
    def get(self, request, pk):
        hotel = HotelRest.objects.get(id=pk)
        serializer = HotelRestSerializer(hotel)
        return Response({'hotel': serializer.data})

    def put(self, request, pk):
        hotel = get_object_or_404(HotelRest.objects.all(), pk=pk)
        data = request.data.get('hotel')
        serializer = HotelRestSerializer(data=data, instance=hotel, partial=True)
        if serializer.is_valid(raise_exception=True):
            new_hotel = serializer.save()
        list_serializer = HotelRestSerializer(new_hotel)
        return Response({'update_hotel': list_serializer.data})

    def delete(self, request, pk):
        hotel = get_object_or_404(ApartmentInfoRest.objects.all(), pk=pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
