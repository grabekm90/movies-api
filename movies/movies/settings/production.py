from . import *

DEBUG = True    # FIXME

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500)
}

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
