from pathlib import Path
import importlib.util
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# If WhiteNoise is not installed (e.g. missed `pip install`), skip it so the site still loads.
# Install `whitenoise` from requirements.txt for compressed static files in production.
_WHITENOISE = importlib.util.find_spec("whitenoise") is not None

# Load environment variables
load_dotenv(BASE_DIR / '.env')

# SECURITY
SECRET_KEY = os.getenv('SECRET', 'django-insecure-dev-key')

# Local dev default is True; set DEBUG=False in production env/.env.
DEBUG = os.getenv('DEBUG', 'True').strip().lower() in ('1', 'true', 'yes', 'on')

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'elenao.pythonanywhere.com',
    'www.elenao.pythonanywhere.com',
]

# Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    *(
        ['whitenoise.middleware.WhiteNoiseMiddleware']
        if _WHITENOISE
        else []
    ),
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Amsterdam'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

# Collected output for production (`collectstatic`). WhiteNoise serves this when DEBUG=False.
STATIC_ROOT = BASE_DIR / 'staticfiles'

if _WHITENOISE:
    STORAGES = {
        'default': {
            'BACKEND': 'django.core.files.storage.FileSystemStorage',
        },
        'staticfiles': {
            'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
        },
    }

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'



# Security
CSRF_TRUSTED_ORIGINS = [
    'https://elenao.pythonanywhere.com',
]

# Messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'