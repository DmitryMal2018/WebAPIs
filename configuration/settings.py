from pathlib import Path
from environs import Env

env = Env()


# Установка переменных окружения. Возьмем переменные окружения из файла .env
env.read_env()


# Установка переменных окружения. Установка базового каталога проекта
BASE_DIR = Path(__file__).resolve().parent.parent


# Установка переменных окружения. Берем секретный ключ из файла .env
# SECRET_KEY = ("django-insecure-p8b=sc$o$!2g+dbuqw6@pn@d7a!-2&3i4%!+edmzgk!)hp5pwh")
SECRET_KEY = env.str("SECRET_KEY")


# Установка переменных окружения. Получаем из файла .env информацию о том, ведем ли мы отладку или нет
# DEBUG = True
DEBUG = env.bool("DEBUG", default=False)


# Список строк, представляющих имена хостов/доменов, которые может обслуживать этот Django-сайт
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Список строк, обозначающих все приложения, которые включены в данной установке Django.
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Сторонние приложения
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "drf_spectacular",
    # Локальные приложения
    "accounts.apps.AccountsConfig",
    "posts.apps.PostsConfig",
]


# Список активизированных промежуточных ПО для использования.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Настройка сервиса статических файлов whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # Настройка механизма в FastAPI приложении
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # Добавим промежуточное ПО для учетной записи:
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "configuration.urls"


# Список, содержащий настройки для всех шаблонизаторов, используемых в Django.
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

WSGI_APPLICATION = "configuration.wsgi.application"


# База данных
DATABASES = {
    # "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3",}
    "default": env.dj_db_url("DATABASE_URL")
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Статические файлы. URL-маршрут, используемый при обращении к статическим файлам (CSS, JavaScript, Images).
STATIC_URL = "static/"
# Хранилище файлов, которое будет использоваться при сборе статических файлов с помощью команды collectstatic
STATICFILES_DIRS = [BASE_DIR / "static"]
# Команда управления для сбора статических файлов в одну директорию, чтобы легко их обслуживать
STATIC_ROOT = BASE_DIR / "staticfiles"
# Механизм хранения файлов, используемый при сборе статических файлов командой collectstatic
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Модель, используемая для представления пользователя
AUTH_USER_MODEL = "accounts.CustomUser"


# Конфигурация для фреймворка REST размещается в единой настройке
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        # Класс разрешения AllowAny разрешает неограниченный доступ, независимо от того,
        # был ли запрос аутентифицирован или неаутентифицирован.
        # "rest_framework.permissions.AllowAny",
        # Класс разрешения IsAuthenticated: неавторизованные пользователи могут
        # просматривать любые страницы, аутентифицированные пользователи имеют
        # права на запись, редактирование или удаление.
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # Cхема аутентификации использует для аутентификации стандартный сессионный бэкенд Django.
        "rest_framework.authentication.SessionAuthentication",
        # Схема аутентификации использует базовую аутентификацию HTTP, подписанную на имя пользователя и пароль.
        # "rest_framework.authentication.BasicAuthentication",
        # Аутентификация с помощью токенов.
        "rest_framework.authentication.TokenAuthentication",
    ],
    # Регистрация drf-spectacular
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


# Список имен хостов origin, которым разрешено выполнять межсайтовые HTTP-запросы.
CORS_ORIGIN_WHITELIST = [
    # Порт по умолчанию для React
    "http://localhost:3000",
    # Порт по умолчанию для Django
    "http://localhost:8000",
]


# Список доверенных источников для небезопасных запросов.
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]


# Конфигурация django-allauth
# Бэкенд, который будет использоваться для отправки электронной почты.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# Целочисленный идентификатор текущего сайта в таблице базы данных django_site.
# Данные приложения могут подключаться к определенным сайтам, а одна база данных могла управлять содержимым нескольких сайтов.
SITE_ID = 1


# Конфигурация drf-spectacular
SPECTACULAR_SETTINGS = {
    "TITLE": "Blog API Project",
    "DESCRIPTION": "A sample blog to learn about DRF",
    "VERSION": "1.0.0",
    # Другие настройки
}
