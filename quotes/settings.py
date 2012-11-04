DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'quotes.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'quotes.db',
    },
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'quotes',
)
