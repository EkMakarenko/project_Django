from django.urls import path
from rest_framework.routers import DefaultRouter

from hotel_rest import views

# 1 способ (Apiview)_______________________________

# urlpatterns = [
#     path('hotelrest', views.HotelCreateReadView.as_view(), name='hotelrest-list'),
#     path('hotelrest/<int:pk>', views.HotelUpdateDeleteView.as_view(), name='hotel-rest-update'),
#     path('apartmentrest', views.ApartmentCreateReadView.as_view(), name='apartment-rest-list'),
#     path('apartmentrest/<int:pk>', views.ApartmentUpdateDeleteView.as_view(), name='apartment-rest-update'),
#     path('apartmentinforest', views.ApartmentInfoCreateReadView.as_view(), name='apartment-info-list'),
#     path('apartmentinforest/<int:pk>', views.ApartmentInfoUpdateDeleteView.as_view(), name='apartment-info-update'),
# ]

# # 2 способ (genericApiview)____________________________________
# urlpatterns = [
#     path('apartmentinforest', views.ApartmentInfoView.as_view(), name='apartment-info-list'),
#     path('apartmentinforest/<int:pk>', views.SingleApartmentInfoView.as_view(), name='apartment-info-update'),
# ]

# 3 способ (ViewSet)____________________________________

router = DefaultRouter()

router.register(r'hotelsrest', views.HotelViewSet, basename='hotels-rest')
router.register(r'apartmentsrest', views.ApartmentViewSet, basename='apartments-rest')
router.register(r'apartmentsinforest', views.ApartmentInfoViewSet, basename='apartments-info-rest')


# urlpatterns += router.urls
urlpatterns = router.urls
