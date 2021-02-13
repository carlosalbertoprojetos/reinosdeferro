import os
from decouple import config
from pathlib import Path
from dj_database_url import parse as dburl



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrapform',
    'ckeditor',
    'reinosdeferro',
    'accounts',
    'social',
    'contato',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projeto.urls'

# processador de contexto, o que faz com que esses valores cadastrados sejam armazenados em um dicionário e fique disponível para ser acessado de todo o projeto. 
# para tanto foi criado o arquivo processors.py em social - o caminho deve ser inserido pasta.arquivo.função 'social.processors.context_processors_social',
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        # 'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.processors.context_processors_social',
            ],
        },
    },
]

WSGI_APPLICATION = 'projeto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

default_dburl = 'sqlite:////'+os.path.join(BASE_DIR,'db.sqlite3')
DATABASES = {'default':config('DATABASE_URL', default=default_dburl, cast=dburl)}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# após efetuar o login, será redirecionado para:
LOGIN_REDIRECT_URL = 'RDF'
LOGOUT_REDIRECT_URL = 'RDF'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-f 
MEDIA_URL = '/media/'

MEDIA_ROOT = 'media'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    'statics'
]
 
STATIC_URL = '/static/'

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '4cbde76bf57cd9'
EMAIL_HOST_PASSWORD = 'f0f092992ce056'
EMAIL_PORT = '2525'

