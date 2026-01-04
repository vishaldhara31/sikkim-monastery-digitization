import os
from pathlib import Path
import dj_database_url
from decouple import config
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")    

# # Secret key & API keys
# # SECRET_KEY = config("SECRET_KEY", default="django-insecure-CHANGE_ME")
# SECRET_KEY = config("SECRET_KEY", default="django-insecure-CHANGE_ME")
# # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_API_KEY = config("OPENAI_API_KEY")

SECRET_KEY = config("SECRET_KEY", default="django-insecure-CHANGE_ME")
OPENAI_API_KEY = config("OPENAI_API_KEY")

# SECURITY WARNING: don’t run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

# Railway requires your domain or * during development
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*").split(",")

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "visitsikkim_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "visitsikkim_project.wsgi.application"

# ------------------------
# Database configuration
# ------------------------

# Default: SQLite (local development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Override with Railway PostgreSQL if DATABASE_URL exists
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL:
    db_from_env = dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)
    DATABASES['default'].update(db_from_env)

# ------------------------
# Password validation
# ------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ------------------------
# Internationalization
# ------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ------------------------
# Static & Media files
# ------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"                       