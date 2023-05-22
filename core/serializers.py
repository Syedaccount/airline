from djoser.serializers import (UserCreateSerializer as BaseUserCreateSerializer,
                                UserSerializer as BaseUserSerializer)
from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "username", "email", "password"]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "last_name", "last_name"]
