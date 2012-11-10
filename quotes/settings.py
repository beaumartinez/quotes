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
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'crispy_forms',
    'django_browserid',
    'floppyforms',

    'quotes',
)

TEMPLATE_DIRS = (
    'quotes/templates',
)

AUTHENTICATION_BACKENDS = (
    'django_browserid.auth.BrowserIDBackend',
)

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

# django_browserid settings

SITE_URL = 'http://quoteb.in/'
