from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор выполняет сериализацию данных для модели User"""

    class Meta:
        model = User
        fields = "__all__"
