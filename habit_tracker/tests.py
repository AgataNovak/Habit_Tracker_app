from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from users.models import User
from habit_tracker.models import Habit, NiceHabit


class HabitTestCase(APITestCase):
    """Класс тестирования эндпоинтов модели Habit"""

    def setUp(self):
        self.user = User.objects.create(email="agata_gorskaia@example.com")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            action="Пить 2 стакана воды",
            is_nice=False,
            reward="Прогулка по пляжу",
            publicity=True,
        )

    def test_habit_retrieve(self):
        url = reverse("habit_tracker:habit_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_update(self):
        url = reverse("habit_tracker:habit_update", args=(self.habit.pk,))
        data = {
            "reward": "Прогулка по парку",
            "publicity": False,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "Пить 2 стакана воды")

    def test_habit_delete(self):
        url = reverse("habit_tracker:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_create(self):
        data = {
            "action": "Пить 2 стакана воды",
            "is_nice": False,
            "reward": "Прогулка по пляжу",
            "publicity": True,
        }
        url = reverse("habit_tracker:habit_create")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.json()
        self.assertEqual(data.get("action"), "Пить 2 стакана воды")


class NiceHabitTestCase(APITestCase):
    """Класс тестирования эндпоинтов модели Habit"""

    def setUp(self):
        self.user = User.objects.create(email="agata_gorskaia@example.com")
        self.client.force_authenticate(user=self.user)
        self.habit = NiceHabit.objects.create(
            owner=self.user,
            action="Прогулка по пляжу",
            is_nice=True,
        )

    def test_habit_retrieve(self):
        url = reverse("habit_tracker:nice_habit_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_update(self):
        url = reverse("habit_tracker:nice_habit_update", args=(self.habit.pk,))
        data = {
            "action": "Прогулка по парку",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "Прогулка по парку")

    def test_habit_delete(self):
        url = reverse("habit_tracker:nice_habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_create(self):
        data = {
            "action": "Прогулка по пляжу",
            "is_nice": True,
        }
        url = reverse("habit_tracker:nice_habit_create")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.json()
        self.assertEqual(data.get("action"), "Прогулка по пляжу")
