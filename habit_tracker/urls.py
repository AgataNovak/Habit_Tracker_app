from django.urls import path

from habit_tracker.apps import HabitTrackerConfig

from .views import (
    HabitCreateAPIView,
    HabitListAPIView,
    HabitUpdateAPIView,
    HabitRetrieveAPIView,
    HabitDestroyAPIView,
    NiceHabitCreateAPIView,
    NiceHabitRetrieveAPIView,
    NiceHabitUpdateAPIView,
    NiceHabitDestroyAPIView,
    NiceHabitListAPIView,
    OwnersHabitsListAPIView,
    OwnersNiceHabitsListAPIView,
)

app_name = HabitTrackerConfig.name

urlpatterns = [
    path("habits/", HabitListAPIView.as_view(), name="habits_list"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path(
        "habit/<int:pk>/delete/",
        HabitDestroyAPIView.as_view(),
        name="habit_delete",
    ),
    path(
        "my_habits/",
        OwnersHabitsListAPIView.as_view(),
        name="my_habits_list",
    ),
    path("nice_habits/", NiceHabitListAPIView.as_view(), name="nice_habits_list"),
    path(
        "nice_habit/<int:pk>/",
        NiceHabitRetrieveAPIView.as_view(),
        name="nice_habit_retrieve",
    ),
    path(
        "nice_habit/create/", NiceHabitCreateAPIView.as_view(), name="nice_habit_create"
    ),
    path(
        "nice_habit/<int:pk>/update/",
        NiceHabitUpdateAPIView.as_view(),
        name="nice_habit_update",
    ),
    path(
        "nice_habit/<int:pk>/delete/",
        NiceHabitDestroyAPIView.as_view(),
        name="nice_habit_delete",
    ),
    path(
        "my_nice_habits/",
        OwnersNiceHabitsListAPIView.as_view(),
        name="my_nice_habits_list",
    ),
]
