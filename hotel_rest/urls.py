from django.urls import path

from hotel_rest import views

urlpatterns = [
    path('hotelrest', views.HotelCreateReadView.as_view(), name='hotelrest-list'),
    path('hotelrest/<int:pk>', views.HotelUpdateDeleteView.as_view(), name='hotel-rest-update'),
    path('apartmentrest', views.ApartmentCreateReadView.as_view(), name='apartment-rest-list'),
    path('apartmentrest/<int:pk>', views.ApartmentUpdateDeleteView.as_view(), name='apartment-rest-update'),
    path('apartmentinforest', views.ApartmentInfoCreateReadView.as_view(), name='apartment-info-list'),
    path('apartmentinforest/<int:pk>', views.ApartmentInfoUpdateDeleteView.as_view(), name='apartment-info-update'),
]
