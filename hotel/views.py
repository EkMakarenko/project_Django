from django.shortcuts import render
from django.urls import reverse
from django.views import generic

# from comment.form import CommentForm
from hotel.form import HotelForm
from hotel.models import Hotel, Apartment, HotelApartment


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

    def form_valid(self, form, apartment=None):
        response = super().form_valid(form)
        selected_apartment = form.cleaned_data.get('apartment')

        apartment_hotel_objects = [
            HotelApartment(hotel=self.object, apartment=apartment)
            for apartment in selected_apartment
        ]
        HotelApartment.objects.bulk_create(apartment_hotel_objects)
        return response

    def get_success_url(self):
        return reverse('hotel-list')


class HotelUpdateView(generic.UpdateView):
    model = Hotel
    template_name = 'hotel/hotel_update.html'
    form_class = HotelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.filter(is_deleted=False)
        return context

    def get_success_url(self):
        return reverse('hotel-list')

