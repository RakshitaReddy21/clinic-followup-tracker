from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER ="reddyrakshita707@gmail.com"
EMAIL_HOST_PASSWORD = "tkmcqqjmwpgqtcyz"
DEFAULT_FROM_EMAIL ="reddyrakshita707@gmail.com"


import os
from dotenv import load_dotenv

load_dotenv()
import pymysql
pymysql.install_as_MySQLdb()


load_dotenv(BASE_DIR / ".env")
SECRET_KEY = 'dev-secret'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
 'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
 'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
 'clinic',
]
MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
]
ROOT_URLCONF = 'clinic_tracker.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'clinic_tracker.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
STATIC_URL='static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
LOGIN_URL='/login/'
LOGIN_REDIRECT_URL='/dashboard/'
