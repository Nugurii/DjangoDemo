from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    """序列化"""
    class Meta:
        model = User
        fields = ("username", "password")