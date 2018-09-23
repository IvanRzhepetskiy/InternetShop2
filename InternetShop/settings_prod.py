DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'django_shop',
        'PASSWORD': '12345asdfghjklAsd',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}