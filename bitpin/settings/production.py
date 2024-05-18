from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        "ENGINE": os.environ.get("POSTGRES_ENGINE", "django.db.backends.postgresql_psycopg2"),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

