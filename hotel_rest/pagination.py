from rest_framework import pagination


class HotelPagination(pagination.PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 20


class ApartmentInfoPagination(pagination.PageNumberPagination):

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20
