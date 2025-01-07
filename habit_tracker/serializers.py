from rest_framework.serializers import ModelSerializer

from .models import Habit

from .validators import (
    RewardsValidator,
    DurationValidator,
    RelatedHabitValidator,
    PeriodicityValidator,
)


class HabitSerializer(ModelSerializer):
    """Сериализатор выполняет сериализацию данных для модели Habit"""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RewardsValidator,
            DurationValidator,
            RelatedHabitValidator,
            PeriodicityValidator,
        ]


class NiceHabitSerializer(ModelSerializer):
    """Сериализатор выполняет сериализацию данных для модели Habit"""

    class Meta:
        model = Habit
        fields = "__all__"
