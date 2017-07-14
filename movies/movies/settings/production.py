from . import *

DEBUG = os.getenv('DJANGO_DEBUG') == '1'

ALLOWED_HOSTS = ['*']   # FIXME

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500)
}

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)
