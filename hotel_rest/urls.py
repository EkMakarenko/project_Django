from django.urls import path
from rest_framework.routers import DefaultRouter

from hotel_rest import views


router = DefaultRouter()

router.register(r'hotelsrest', views.HotelViewSet, basename='hotels-rest')
# router.register(r'apartmentsrest', views.ApartmentViewSet, basename='apartments-rest')
router.register(r'apartmentsinforest', views.ApartmentInfoViewSet, basename='apartments-info-rest')


# urlpatterns += router.urls
urlpatterns = router.urls
