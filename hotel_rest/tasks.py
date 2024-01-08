from celery import shared_task

from hotel_rest.models import ApartmentInfoRest, HotelRest


@shared_task
def delete_deleted_apartments():
    deleted_apartments = ApartmentInfoRest.objects.filter(is_deleted=True)
    deleted_apartments.delete()


@shared_task
def delete_deleted_hotels():
    deleted_hotels = HotelRest.objects.filter(is_deleted=True)
    deleted_hotels.delete()


@shared_task
def print_message():
    print(';)')


