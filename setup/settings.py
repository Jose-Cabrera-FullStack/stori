"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import environ
from os import getenv as env
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qq(lp@!9q)m@#6^tip^9552-z(c8qys5b82!iwv0)is$d8t4z='


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'django_celery_results',
    'django_celery_beat',
    "drf_standardized_errors",
    'stori'
]

ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            './stori/templates/transactions/'
        ],
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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(env('DB_NAME')),
        'USER': str(env('DB_USER')),
        'PASSWORD': str(env('DB_PASSWORD')),
        'HOST': str(env('DB_HOST')),
        'PORT': str(env('DB_PORT'))
    },
}

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'drf_standardized_errors.handler.exception_handler',
    'DEFAULT_RENDERER_CLASSES': [
        'setup.response_formatter.ApiRenderer',
        'rest_framework.renderers.JSONRenderer',
    ],
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Send email settings
# EMAIL_BACKEND = str(
#     env("EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"))
# EMAIL_HOST = str(env("EMAIL_BACKEND", default=""))
# EMAIL_PORT = env("EMAIL_BACKEND", default=587)
# EMAIL_USE_TLS = env("EMAIL_BACKEND", default=True)
# EMAIL_HOST_USER = str(env("EMAIL_BACKEND", default=""))
# EMAIL_HOST_PASSWORD = str(env("EMAIL_BACKEND", default=""))
# EMAIL_FROM = str(env("EMAIL_BACKEND", default=""))

# TODO: It has to be a env variable
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'murdoc.jose.6@gmail.com'
EMAIL_HOST_PASSWORD = 'ajxaehehnmgelxeq'
EMAIL_FROM = 'jose.miguel.cabrera.prieto@gmail.com'

# ---- Celery
redis_internal_location = str(env('REDIS_INTERNAL_URL', default=None))

BROKER_URL = str(env("CELERY_BROKER_URL"))
CELERY_RESULT_BACKEND = str(env("CELERY_BROKER_URL"))
FORKED_BY_MULTIPROCESSING = 1

S3_AWS_REGION = str(env("S3_AWS_REGION", default=""))
S3_ACCESS_KEY = str(env("S3_ACCESS_KEY", default=""))
S3_SECRET_KEY = str(env("S3_SECRET_KEY", default=""))
S3_BUCKET_NAME = str(env("S3_BUCKET_NAME", default=""))

CLOUDWATCH_AWS_REGION = str(env("CLOUDWATCH_AWS_REGION", default=""))
CLOUDWATCH_ACCESS_KEY = str(env("CLOUDWATCH_ACCESS_KEY", default=""))
CLOUDWATCH_SECRET_KEY = str(env("CLOUDWATCH_SECRET_KEY", default=""))
CLOUDWATCH_GROUP_NAME = str(env("CLOUDWATCH_GROUP_NAME", default=""))

MS_NAME = str(env("MS_NAME", default=""))
