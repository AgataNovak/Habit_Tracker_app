from .API_services import send_telegram_message

from users.models import User

from .models import Habit


def send_telegram_notification():
    """Функция производит поиск данных о привычках всех зарегистрированных пользователей
    и вызывает команду отправки telegram уведомления по списку пользователей, у которых указан ник telegram
    """

    users = User.objects.all()
    users_id_list = []
    for user in users:
        user_id = dict(user).get("id")
        users_id_list.append(user_id)
    for user in users_id_list:
        habits = Habit.objects.filter(owner=user)
        habits_clear = {}
        for habit in habits:
            habit_action = dict(habit).get("action")
            habit_time = dict(habit).get("time")
            habits_clear.update({habit_action: habit_time})
        habits_clear = list(habits_clear.items())
        user = User.objects.filter(id=user).get("telegram_name")
        if user:
            send_telegram_message(user, f'Ваши привычки на сегодня: "{habits_clear}"')
