# Generated by Django 5.0 on 2023-12-29 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_rest', '0002_remove_apartmentinforest_is_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentinforest',
            name='apartment_id',
        ),
    ]
