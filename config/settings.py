import os
import sys
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = os.getenv("DJANGO_SECRETE_KEY")
SECRET_KEY = "django-insecure-*m-pd&06$rt1ho=%k#3+k%fe71%#wf9wvzgif557j*pdrks$g#"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "django_celery_beat",
    "django_filters",
    "drf_yasg",
    "users",
    "habit_tracker",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

CELERY_BROKER_URL = "redis://redis:6379"

CELERY_RESULT_BACKEND = "redis://redis:6379"

CELERY_TIMEZONE = TIME_ZONE

CELERY_TASK_TRACK_STARTED = True

CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_BEAT_SCHEDULE = {
    "update_notification_email": {
        "task": "habit_tracker_app_project.habit_tracker.tasks.telegram_notification",
        "schedule": timedelta(hours=12),
    },
}

TELEGRAM_URL = "https://api.telegram.ord/bot"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://84.201.167.205",
    "https://84.201.167.205",
]

CSRF_TRUSTED_ORIGINS = [
    "https://localhost:8000",
    "http://84.201.167.205",
    "https://84.201.167.205",
]

CORS_ALLOW_ALL_ORIGINS = False

LOGIN_REDIRECT_URL = "habit_tracker:habits_list"

LOGIN_URL = "users:login"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379/1",
    }
}

if "test" in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "test_db_sqlite3",
        }
    }
