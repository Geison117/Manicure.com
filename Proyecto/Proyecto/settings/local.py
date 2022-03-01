from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'afdpxjwd',
        'USER': 'afdpxjwd',
        'PASSWORD': 'gC0HklelN2j8yLBW51YSr5TAhXcJAAsA',
        'HOST': 'castor.db.elephantsql.com',
        'PORT': '' ,
    }
}