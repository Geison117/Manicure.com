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
        'NAME': 'tnjvcgxr',
        'USER': 'tnjvcgxr',
        'PASSWORD': 'ENQ5dAClZsa3Ib5IA2jmBbAhOf7O6B-A',
        'HOST': 'jelani.db.elephantsql.com',
        'PORT': '' ,
    }
}