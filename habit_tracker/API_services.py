from dotenv import load_dotenv
import requests
import os
from config import settings

load_dotenv()


def send_telegram_message(chat_id, message):
    """Функция использует API приложения telegram, отправляя через подключенного бота сообщение пользователю"""

    params = {"text": message, "chat_id": chat_id}

    response = requests.get(
        f"{settings.TELEGRAM_URL}{os.getenv('BOT_TOKEN')}/sendMessage", params=params
    )
    return response.status_code
