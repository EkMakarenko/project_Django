from django.urls import path
from hotel import views

urlpatterns = [
    path('hotel', views.HotelListView.as_view(), name='hotel-list'),
    # path('apartment', views.ApartmentListView.as_view(), name='apartment-list'),
    path('hotel/<int:pk>', views.HotelDetailView.as_view(), name='hotel-detail'),
    # path('hotel/<int:pk>/', views.ApartmentDetailView.as_view(), name='apartment-detail'),
    path('hotel/create', views.HotelCreateView.as_view(), name='hotel-create'),
    path('hotel/<int:pk>/update', views.HotelUpdateView.as_view(), name='hotel-update'),
]