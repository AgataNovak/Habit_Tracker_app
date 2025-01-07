import datetime

from rest_framework.serializers import ValidationError

from .models import NiceHabit


class RewardsValidator:
    """Валидатор проверяет, что для модели Полезной Привычки выбрана либо Приятная привычка, либо вознаграждение"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        nice_habit = dict(value).get("nice_habit")
        reward = dict(value).get("reward")
        if nice_habit:
            if reward:
                raise ValidationError
        elif reward:
            if nice_habit:
                raise ValidationError


class DurationValidator:
    """Валидатор проверяет, что продолжительность (время выполнения) привычки не превышает 120 секунд"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get("duration")
        allowed_time = datetime.timedelta(seconds=120)
        if duration >= allowed_time:
            raise ValidationError


class RelatedHabitValidator:
    """Валидатор проверяет, что в поле Связанной Привычки указан объект модели Приятная Привычка"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = dict(value).get("related_habit")
        if not isinstance(related_habit, NiceHabit):
            raise ValidationError


class PeriodicityValidator:
    """Валидатор проверяет, что в поле Периодичность Привычки указано значение не более 7 дней"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get("periodicity")
        if periodicity > 7:
            raise ValidationError
