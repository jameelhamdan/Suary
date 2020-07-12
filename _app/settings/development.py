from .base import *
import django_heroku
django_heroku.settings(
    locals(),
    databases=False,
    staticfiles=False
)

DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "../public")
STATICFILES_DIRS = []
