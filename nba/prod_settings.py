from .settings import *

import dj_database_url

DATABASES['default'] = dj_database_url.config(conn_max_age=20, ssl_require=True)

STATIC_ROOT = 'staticfiles'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = False