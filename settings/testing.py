import dj_database_url
from .base import *

DEBUG = False

# Database
DATABASES = {
    'default': dj_database_url.config()
}
