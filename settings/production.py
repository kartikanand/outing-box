"""
outingbox
=========

settings for production environments

"""

import dj_database_url
from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

# Database
DATABASES = {
    'default': dj_database_url.config()
}

# Django all auth
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

#CACHES = {
#    'default': {
#        'BACKEND': 'django_redis.cache.RedisCache',
#        'LOCATION': 'redis://127.0.0.1:6379/1',
#        'OPTIONS': {
#            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
#        }
#    },
#    'cache_session': {
#        'BACKEND': 'django_redis.cache.RedisCache',
#        'LOCATION': 'redis://127.0.0.1:6379/2',
#        'OPTIONS': {
#            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
#        }
#    }
#}
#
#CACHE_MIDDLEWARE_ALIAS = 'default'
#CACHE_MIDDLEWARE_SECONDS = 60*60
#CACHE_MIDDLEWARE_KEY_PREFIX = ''
#
#SESSION_CACHE_ALIAS = 'cache_session'
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
