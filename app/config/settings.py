import os
from pathlib import Path
import dj_database_url

# IMPORTANTE: tu manage.py está dentro de app/
# Entonces BASE_DIR debe subir DOS niveles:
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

AUTH_USER_MODEL = 'users.User'

DEBUG = os.environ.get('DEBUG', 'false') == 'true'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# ---------------- STATIC FILES ---------------- #

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ESTA es la ubicación correcta:
# tu carpeta static está en: app/static/
STATICFILES_DIRS = [
    BASE_DIR / "app" / "static",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ---------------- INSTALLED APPS ---------------- #

INSTALLED_APPS = [
    'users',
    'appointments',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ---------------- MIDDLEWARE ---------------- #

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "app" / "templates"],
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

WSGI_APPLICATION = 'config.wsgi.application'

# ---------------- DATABASE ---------------- #

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# ---------------- GLOBAL SETTINGS ---------------- #

LANGUAGE_CODE = 'es'
TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
