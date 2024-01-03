from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

from authentication.models import Gender, CustomUser


class UserSerializer(BaseUserSerializer):

    phone_number = serializers.CharField()
    gender = serializers.ChoiceField(choices=[(gender.name, gender.value) for gender in Gender])
    birth_date = serializers.DateField()
    country = serializers.DateField()
    city = serializers.DateField()

    class Meta(BaseUserSerializer.Meta):
        fields = (
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


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = (
            'username',
            'email',
            'phone_number',
            'password'
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
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
