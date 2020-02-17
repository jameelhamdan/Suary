import os
import mongoengine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY', 'y#(a2(nm=98!xe48ozi-81o7r7#&8s68x6j0@323ciq&3yq%^#')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
APPEND_SLASH = False

ADMINS = [('Jameel Hamdan', 'jameelhamdan99@yahoo.com')]


# Application definition
INSTALLED_APPS = [
    'rest_framework',
    'auth',
    'media',
    'users',
    'main',
]

MIDDLEWARE = [
    'auth.backend.middleware.AuthMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '_settings.urls'


WSGI_APPLICATION = '_settings.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
}

# Authentication settings
REFRESH_TOKEN_EXPIRATION_PERIOD = 60 * 24 * 14
AUTH_TOKEN_EXPIRATION_PERIOD = 60


# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DEFAULT_DATABASE_NAME', 'main'),
        'USER': os.getenv('DEFAULT_DATABASE_USER', 'postgres'),
        'PASSWORD': os.getenv('DEFAULT_DATABASE_PASS', '1234'),
        'HOST': os.getenv('DEFAULT_DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DEFAULT_DATABASE_PORT', ''),
    }
}

# mongodb database connection
MONGO_DEFAULT_DATABASE_URL = os.getenv('MONGO_DEFAULT_DATABASE_URL', 'localhost:27017')
MONGO_DEFAULT_DATABASE_NAME = os.getenv('MONGO_DEFAULT_DATABASE_NAME', 'default_storage')

MONGO_MEDIA_DATABASE_URL = os.getenv('MONGO_MEDIA_DATABASE_URL', 'localhost:27017')
MONGO_MEDIA_DATABASE_NAME = os.getenv('MONGO_MEDIA_DATABASE_NAME', 'media_storage')

mongoengine.connect(MONGO_DEFAULT_DATABASE_NAME, host=MONGO_DEFAULT_DATABASE_URL, alias='default', maxpoolsize=500)
mongoengine.connect(MONGO_MEDIA_DATABASE_NAME, host=MONGO_MEDIA_DATABASE_URL, alias='media_database', maxpoolsize=500)


# Custom
MEDIA_FORMATS = ['png', 'jpeg', 'jpg', 'gif', 'mp4', 'm4a', 'm4v', 'webm']
AVATAR_FORMATS = ['png', 'jpeg', 'jpg']
