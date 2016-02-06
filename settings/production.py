"""
outingbox
=========

settings for production environments

"""

import dj_database_url
from .base import *

THUMBNAIL_DEBUG = False
DEBUG = False

# Database
DATABASES = {
    'default': dj_database_url.config()
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    },
    'cache_session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60*60
CACHE_MIDDLEWARE_KEY_PREFIX = ''

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = 'cache_session'
