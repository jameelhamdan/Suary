import os
import django.db.models.options
import dj_database_url

django.db.models.options.DEFAULT_NAMES = django.db.models.options.DEFAULT_NAMES + ('db',)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY', 'y#(a2(nm=98!xe48ozi-81o7r7#&8s68x6j0@323ciq&3yq%^#')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
APPEND_SLASH = False

ADMINS = [('Jameel Hamdan', 'jameelhamdan99@yahoo.com')]

# Application definition
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'auth',
    'media',
    'users',
    'main',
    'feed',
    'frontend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auth.backend.middleware.AuthMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = '_app.urls'

WSGI_APPLICATION = '_app.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/public/'
SERVE_FRONTEND = os.getenv('SERVE_FRONTEND', True)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../public")
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# Templating
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                '_common.context_processors.settings_export',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
    'UNAUTHENTICATED_USER': None,
}

API_PREFIX = 'api'
# TODO: Setup proper cross origin policy for dev environment
CORS_ORIGIN_ALLOW_ALL = True

# Authentication settings
REFRESH_TOKEN_EXPIRATION_PERIOD = os.getenv('REFRESH_TOKEN_EXPIRATION_PERIOD', 60 * 24 * 14)
AUTH_TOKEN_EXPIRATION_PERIOD = os.getenv('REFRESH_TOKEN_EXPIRATION_PERIOD', 60 * 24)

# Databases
DEFAULT_DATABASE = 'default'
MEDIA_DATABASE = 'media'

DATABASES = {
    DEFAULT_DATABASE: dj_database_url.parse(os.getenv('DEFAULT_DATABASE_URL', 'postgres://postgres:1234@127.0.0.1:5432/main')),
    MEDIA_DATABASE: {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propogate': False,
                    'handlers': ['console']
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG'
                }
            }
        },
        'NAME': 'media',
        'CONN_MAX_AGE': 600,
        'CLIENT': {
            'host': os.getenv('MEDIA_DATABASE_URL', 'mongodb://localhost:27017'),
            'minPoolSize': 1,
            'maxPoolSize': 100,
        }
    }
}

DATABASE_ROUTERS = ['_app.db_routers.Router', ]

# Custom
MEDIA_FORMATS = ['png', 'jpeg', 'jpg', 'gif', 'mp4', 'm4a', 'm4v', 'webm', 'webp']
IMAGE_FORMATS = ['png', 'jpeg', 'jpg', 'gif']
AVATAR_FORMATS = ['png', 'jpeg', 'jpg']
