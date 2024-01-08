
from django_filters import rest_framework as django_filters
from rest_framework.decorators import action
from rest_framework import status, viewsets, generics, mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from hotel_rest.filters import HotelFilter, ApartmentInfoFilter
from hotel_rest.models import ApartmentInfoRest, HotelRest
from hotel_rest.pagination import ApartmentInfoPagination, HotelPagination
from hotel_rest.permissions import IsOwnerOrReadOnlyPermission
from hotel_rest.serializers import (
    ApartmentInfoListSerializer,
    ApartmentInfoCreateSerializer,
    ApartmentInfoRetrieveSerializer,
    ApartmentInfoUpdateSerializer,
    ApartmentInfoRecentSerializer,
    HotelListSerializer,
    HotelCreateSerializer,
    HotelRetrieveSerializer,
    HotelUpdateSerializer,
    HotelRecentSerializer, ApartmentInfoImageUpdateSerializer, HotelImageUpdateSerializer,
)
from hotel_rest.services import ImageService


class ApartmentInfoViewSet(viewsets.ModelViewSet):
    queryset = ApartmentInfoRest.available_objects.all()
    serializer_class = ApartmentInfoListSerializer

    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    # filterset_class = ApartmentInfoFilter
    # ordering_fields = ('id', 'numer_of_beds', 'total_area', 'number_of_bathroom', 'price')
    # search_fields = ('numer_of_beds', 'total_area', 'number_of_bathroom', 'price', 'hotel__name')
    # pagination_class = ApartmentInfoPagination
    # permission_classes = (IsOwnerOrReadOnlyPermission, )

    serializer_classes = {
        'list': ApartmentInfoListSerializer,
        'create': ApartmentInfoCreateSerializer,
        'retrieve': ApartmentInfoRetrieveSerializer,
        'update': ApartmentInfoUpdateSerializer,
        'partial-update': ApartmentInfoUpdateSerializer,
        'recent_apartments': ApartmentInfoRecentSerializer,
        'update_image': ApartmentInfoImageUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def destroy(self, request, *args, **kwargs):
        apartment_info = self.get_object()
        apartment_info.is_deleted = True
        apartment_info.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='resent_apartments')
    def resent_apartments(self, request):
        resent_apartments = ApartmentInfoRest.objects.filter(price__gte=50)
        serializer = self.serializer_classes.get(self.action, self.serializer_class)(resent_apartments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], url_path='update-image')
    def update_image(self, request, pk=None):
        apartment = self.get_object()
        serializer = self.serializer_classes.get(self.action, self.serializer_class)(apartment, request.data, partial=True)

        ImageService.update_image(serializer=serializer, instance=apartment, request=request)

        self.perform_update(serializer)
        return Response(serializer.data)


class HotelViewSet(viewsets.ModelViewSet):
    queryset = HotelRest.objects.all()
    serializer_class = HotelListSerializer
    # filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    # filterset_class = HotelFilter
    # ordering_fields = ('id', 'country', 'name', 'rating',)
    # ordering = ('-rating', )
    # # search_fields = ('country', 'city', 'name', 'rating',)
    # pagination_class = HotelPagination
    # permission_classes = (IsAuthenticated, )

    serializer_classes = {
        'list': HotelListSerializer,
        'create': HotelCreateSerializer,
        'retrieve': HotelRetrieveSerializer,
        'update': HotelUpdateSerializer,
        'partial-update': HotelUpdateSerializer,
        'recent_hotels': HotelRecentSerializer,
        'update_image': HotelImageUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @action(detail=False, methods=['get'], url_path='resent_hotel')
    def resent_hotel(self, request):
        resent_hotel = HotelRest.objects.filter(rating__gte=6)
        serializer = self.serializer_classes.get(self.action, self.serializer_class)(resent_hotel, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], url_path='update-image')
    def update_image(self, request, pk=None):
        hotel = self.get_object()
        serializer = self.serializer_classes.get(self.action, self.serializer_class)(hotel, request.data, partial=True)

        ImageService.update_image(serializer=serializer, instance=hotel, request=request)

        self.perform_update(serializer)
        return Response(serializer.data)
