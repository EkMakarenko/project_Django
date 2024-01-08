import json
import os

import django
from django.apps import apps
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


class HotelViewSetTests(TestCase):

    def setUp(self):
        self.hotel_model = apps.get_model('hotel_rest', 'HotelRest')
        self.hotel_model = apps.get_model('hotel_rest', 'HotelRest')
        self.hotel_data_1 = {
            "id": 1,
            "name": "Bliska Wola",
            "country": "Poland",
            "city": "Warsaw",
            "street": "Marcina",
            "house_number": 29,
            "image_hotel": "null",
            "rating": 9,
            "is_deleted": "False",
            }
        self.hotel_data_2 = {
            "id": 2,
            "name": "Warsaw Apartments",
            "country": "Poland",
            "city": "Warsaw",
            "street": "Wola",
            "house_number": 5,
            "image_hotel": "",
            "rating": 6,
            "is_deleted": "False",
            }
        self.hotel_1 = self.hotel_model.objects.create(**self.hotel_data_1)
        self.hotel_2 = self.hotel_model.objects.create(**self.hotel_data_2)

    def test_list_hotels(self):
        response = self.client.get(path=reverse('hotels-rest-list'))
        hotels = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertTrue(isinstance(hotels, list))
        #
        self.assertEqual(len(hotels), 2)
        #
        # self.assertEqual(hotels[0]["id"], self.hotel_1.id)
        # self.assertEqual(hotels[0]["name"], self.hotel_1.name)
        # self.assertEqual(hotels[0]["country"], self.hotel_1.country)
        # self.assertEqual(hotels[0]["city"], self.hotel_1.city)
        # self.assertEqual(hotels[0]["street"], self.hotel_1.street)
        # self.assertEqual(hotels[0]["house_number"], self.hotel_1.house_number)
        # self.assertEqual(hotels[0]["image_hotel"], self.hotel_1.image_hotel)
        # self.assertEqual(hotels[0]["rating"], self.hotel_1.rating)
        # self.assertEqual(hotels[0]["is_deleted"], self.hotel_1.is_deleted)
        #
        # self.assertEqual(hotels[1]["id"], self.hotel_2.id)
        # self.assertEqual(hotels[1]["name"], self.hotel_2.name)
        # self.assertEqual(hotels[1]["country"], self.hotel_2.country)
        # self.assertEqual(hotels[1]["city"], self.hotel_2.city)
        # self.assertEqual(hotels[1]["street"], self.hotel_2.street)
        # self.assertEqual(hotels[1]["house_number"], self.hotel_2.house_number)
        # self.assertEqual(hotels[1]["image_hotel"], self.hotel_2.image_hotel)
        # self.assertEqual(hotels[1]["rating"], self.hotel_2.rating)
        # self.assertEqual(hotels[1]["is_deleted"], self.hotel_2.is_deleted)

    # def test_create_hotels(self):
    #     hotel_data = {
    #         "name": "Atrium",
    #         "country": "Belarus",
    #         "city": "Mogilev",
    #         "street": "Lenina",
    #         "house_number": 10,
    #         "image_hotel": "",
    #         "rating": 7,
    #         "is_deleted": "False",
    #     }
    #     response = self.client.post(reverse('hotel-list'), hotel_data, format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #     hotel = response.data
    #
    #     self.assertEqual(hotel.id, response.data['id'])
    #     self.assertEqual(hotel.name, hotel_data['name'])
    #     self.assertEqual(hotel.country, hotel_data['country'])
    #     self.assertEqual(hotel.city, hotel_data['city'])
    #     self.assertEqual(hotel.street, hotel_data['street'])
    #     self.assertEqual(hotel.house_number, hotel_data['house_number'])
    #     self.assertEqual(hotel.image_hotel, hotel_data['image_hotel'])
    #     self.assertEqual(hotel.rating, hotel_data['rating'])
    #     self.assertEqual(hotel.is_deleted, hotel_data['is_deleted'])
    #
    # def test_retrieve_hotels(self):
    #     response = self.client.get(path=reverse('hotel-detail', args=[self.hotel_1.id]))
    #
    #     # self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     self.assertEqual(response.data['id'], self.hotel_1.id)
    #     self.assertEqual(response.data["name"], self.hotel_1.name)
    #     self.assertEqual(response.data["country"], self.hotel_1.country)
    #     self.assertEqual(response.data["city"], self.hotel_1.city)
    #     self.assertEqual(response.data["street"], self.hotel_1.street)
    #     self.assertEqual(response.data["house_number"], self.hotel_1.house_number)
    #     self.assertEqual(response.data["image_hotel"], self.hotel_1.image_hotel)
    #     self.assertEqual(response.data["rating"], self.hotel_1.rating)
    #     self.assertEqual(response.data["is_deleted"], self.hotel_1.is_deleted)
    #
    # def test_update_hotels(self):
    #     updated_data = {
    #         'name': 'Metropolis'
    #     }
    #     response = self.client.patch(
    #         reverse('hotel-detail', args=[self.hotel_1.id]),
    #         data=json.dumps(updated_data),
    #         content_type='application/json'
    #     )
    #
    #     # self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     self.assertEqual(updated_data['name'], response.data['name'])
    #
    #     updated_hotel = self.hotel_model.objects.get(id=self.hotel_1.id)
    #
    #     self.assertEqual(updated_data['name'], updated_hotel.name)
    #
    #     self.assertTrue(self.hotel_1.name != updated_hotel.name)
    #
    # def test_delete_hotel(self):
    #     response = self.client.delete(reverse('hotel-detail', args=[self.hotel_1.id]))
    #
    #     # self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #
    #     with self.assertRaises(ObjectDoesNotExist):
    #         deleted_hotel = self.hotel_model.objects.get(id=self.hotel_1.id)

    # def test_apartment_action(self):
    #     apartment1 = self.apartment_model.objects.create(
    #       hotel=self.hotel_1,
    #       numer_of_beds='double',
    #       total_area=20,
    #       number_of_bathroom=1,
    #       price=50,
    #       is_available=True
    #    )
    #
    #     apartment2 = self.apartment_model.objects.create(
    #         hotel=self.hotel_2,
    #         numer_of_beds='double',
    #         total_area=40,
    #         number_of_bathroom=2,
    #         price=100,
    #         is_available=True
    #     )
    #
    #     response = self.client.get(reverse('hotels-apartment', args=[self.hotel_1.id]))
    #
    #     self.assertEqual(response.data[0]['id'], apartment1.id)
    #     self.assertEqual(response.data[0]['hotel'], apartment1.hotel)
    #     self.assertEqual(response.data[0]['numer_of_beds'], apartment1.numer_of_beds)
    #     self.assertEqual(response.data[0]['total_area'], apartment1.total_area)
    #     self.assertEqual(response.data[0]['number_of_bathroom'], apartment1.number_of_bathroom)
    #     self.assertEqual(response.data[0]['price'], apartment1.price)
    #     self.assertEqual(response.data[0]['is_available'], apartment1.is_available)

        # self.assertEqual(response.data[1]['id'], apartment2.id)
        # self.assertEqual(response.data[1]['hotel'], apartment2.hotel)
        # self.assertEqual(response.data[1]['numer_of_beds'], apartment2.numer_of_beds)
        # self.assertEqual(response.data[1]['total_area'], apartment2.total_area)
        # self.assertEqual(response.data[1]['number_of_bathroom'], apartment2.number_of_bathroom)
        # self.assertEqual(response.data[1]['price'], apartment2.price)
        # self.assertEqual(response.data[1]['is_available'], apartment2.is_available)