from django.db import models

from users.models import User


class NiceHabit(models.Model):
    """Модель приятной привычки"""

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
    )
    action = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name="Действие приятной привычки",
        help_text="Введите действие приятной привычки",
    )
    is_nice = models.BooleanField(
        default=True,
        null=True,
        blank=False,
        verbose_name="Признак приятной привычки",
        help_text="Введите признак приятной привычки",
    )

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Приятная привычка"
        verbose_name_plural = "Приятные привычки"


class Habit(models.Model):
    """Модель полезной привычки"""

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
    )
    place = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Место выполнения привычки",
        help_text="Введите место выполнения привычки",
    )
    time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Время выполнения привычки",
        help_text="Укажите время выполнения привычки",
    )
    action = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Действие представляющее привычку",
        help_text="Введите действие представляющее привычку",
    )
    is_nice = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name="Признак приятной привычки",
        help_text="Введите признак приятной привычки",
    )
    related_habit = models.ForeignKey(
        NiceHabit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
    )
    periodicity = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        verbose_name="Периодичность выполнения привычки в днях",
        help_text="Укажите периодичность выполнения привычки в днях",
    )
    reward = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Вознаграждение за выполнение привычки",
        help_text="Введите вознаграждение за выполнение привычки",
    )
    duration = models.DurationField(
        null=True,
        blank=True,
        verbose_name="Продолжительность выполнения привычки",
        help_text="Введите продолжительность выполнения привычки",
    )
    publicity = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name="Публичность привычки",
        help_text="Введите публичность привычки",
    )

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Полезная привычка"
        verbose_name_plural = "Полезные привычки"
