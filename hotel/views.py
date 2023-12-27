from django.shortcuts import render
from django.urls import reverse
from django.views import generic

# from comment.form import CommentForm
from hotel.form import HotelForm
from hotel.models import Hotel, Apartment


# Create your views here.


def read_post(request):
    return render(request, 'info.html')


class HotelListView(generic.ListView):
    template_name = 'hotel/hotel_list.html'
    context_object_name = 'hotel'
    queryset = Hotel.objects.filter(is_deleted=False)


class HotelDetailView(generic.DetailView):
    model = Hotel
    template_name = 'hotel/hotel_detail.html'
    context_object_name = 'hotel_detail'
    # form = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.filter(is_deleted=False)
        return context


    def get_success_url(self):
        return reverse('hotel-list')


class HotelCreateView(generic.CreateView):
    template_name = 'hotel/hotel_create.html'
    form_class = HotelForm


class HotelUpdateView(generic.UpdateView):
    model = Hotel
    template_name = 'hotel/hotel_update.html'
    form_class = HotelForm

    def get_success_url(self):
        return reverse('hotel-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.filter(is_deleted=False)
        return context