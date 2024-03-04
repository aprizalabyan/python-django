from rest_framework import serializers
from .models import User, user_collection


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["_id", "name", "email", "createdAt", "updatedAt"]
