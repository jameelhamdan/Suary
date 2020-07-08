from .base import *
import django_heroku
django_heroku.settings(
    locals(),
    databases=False,
    staticfiles=False
)

DEBUG = False
