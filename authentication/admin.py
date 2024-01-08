from django.contrib import admin

from authentication.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'username',
        'email',
        'phone_number',
        'gender',
        'birth_date',
        'country',
        'city'
    )
