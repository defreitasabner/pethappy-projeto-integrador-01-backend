"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$)udpti#b@yegq$k8zd66=t&(27qz%4!tp&gu^59i4d!vi5s9q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',
    'django_filters',
    'pessoas',
    'pets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3'),
#        'NAME': os.environ.get('DB_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
#        'USER': os.environ.get('DB_USER', None),
#        'PASSWORD': os.environ.get('DB_PASSWORD', None),
#        'HOST': os.environ.get('DB_HOST', None),
#        'PORT': os.environ.get('DB_PORT', None),
#    }
#}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.oracle',
#        'NAME': 'PetHappyDB',  # Nome do seu banco de dados
#        'USER': 'ADMIN',  # Nome do usuário do banco de dados
#        'PASSWORD': 'P3tH@ppYD@t@B@s3',  # Senha do usuário
#        'HOST': 'adb.sa-saopaulo-1.oraclecloud.com',  # Endereço do host, geralmente é o endpoint do Autonomous Database
#        'PORT': '1522',  # Porta padrão para Oracle
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.sa-saopaulo-1.oraclecloud.com))(connect_data=(service_name=gc085d3344163a8_pethappydb_tpurgent.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))',
        'USER': 'ADMIN',
        'PASSWORD': 'P3tH@ppYD@t@B@s3',
        'HOST': '',  # Deixe em branco, pois está no DSN
        'PORT': '',  # Deixe em branco, pois está no DSN
        'OPTIONS': {
            'config_dir': 'C:/Projetos/PetHappyBack/pethappy-projeto-integrador-01-backend/infra/oracledb',
            'wallet_location': 'C:/Projetos/PetHappyBack/pethappy-projeto-integrador-01-backend/infra/oracledb',
            'wallet_password': 'dsf29788',
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Django Rest Framework Settings

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',        
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS Settings
CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200',
]
