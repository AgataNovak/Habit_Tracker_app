from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)

from .serializers import HabitSerializer, NiceHabitSerializer

from .models import NiceHabit, Habit

from .paginators import NiceHabitPaginator, HabitPaginator

from users.permissions import IsOwner

from rest_framework.permissions import AllowAny, IsAuthenticated


class NiceHabitCreateAPIView(CreateAPIView):
    """Контроллер создания объекта класса NiceHabit"""

    queryset = NiceHabit.objects.all()
    serializer_class = NiceHabitSerializer
    permission_classes = [
        IsOwner,
    ]


class NiceHabitRetrieveAPIView(RetrieveAPIView):
    """Контроллер просмотра объекта класса NiceHabit"""

    queryset = NiceHabit.objects.all()
    serializer_class = NiceHabitSerializer
    permission_classes = [
        IsOwner,
    ]


class NiceHabitUpdateAPIView(UpdateAPIView):
    """Контроллер обновления объекта класса NiceHabit"""

    queryset = NiceHabit.objects.all()
    serializer_class = NiceHabitSerializer
    permission_classes = [
        IsOwner,
    ]


class NiceHabitDestroyAPIView(DestroyAPIView):
    """Контроллер удаления объекта класса NiceHabit"""

    queryset = NiceHabit.objects.all()
    serializer_class = NiceHabitSerializer
    permission_classes = [
        IsOwner,
    ]


class NiceHabitListAPIView(ListAPIView):
    """Контроллер просмотра списка объектов класса NiceHabit"""

    queryset = NiceHabit.objects.all()
    serializer_class = NiceHabitSerializer
    permission_classes = [
        AllowAny,
    ]
    pagination_class = NiceHabitPaginator


class HabitCreateAPIView(CreateAPIView):
    """Контроллер создания объекта класса Habit"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [
        IsOwner,
    ]


class HabitRetrieveAPIView(RetrieveAPIView):
    """Контроллер просмотра объекта класса Habit"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [
        IsOwner,
    ]


class HabitUpdateAPIView(UpdateAPIView):
    """Контроллер обновления объекта класса Habit"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [
        IsOwner,
    ]


class HabitDestroyAPIView(DestroyAPIView):
    """Контроллер удаления объекта класса Habit"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [
        IsOwner,
    ]


class HabitListAPIView(ListAPIView):
    """Контроллер просмотра списка объектов класса Habit"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [
        AllowAny,
    ]
    pagination_class = HabitPaginator


class OwnersHabitsListAPIView(ListAPIView):
    """Контроллер просмотра списка объектов класса Habit принадлежащих авторизованному пользователю"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)


class OwnersNiceHabitsListAPIView(ListAPIView):
    """Контроллер просмотра списка объектов класса NiceHabit принадлежащих авторизованному пользователю"""

    queryset = NiceHabit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)
