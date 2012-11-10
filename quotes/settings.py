from django.core.urlresolvers import reverse_lazy

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

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

AUTHENTICATION_BACKENDS = (
    'django_browserid.auth.BrowserIDBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django_browserid.context_processors.browserid_form',
)

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

LOGIN_REDIRECT_URL = reverse_lazy('landing')
LOGIN_URL = reverse_lazy('log_in')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

# django_browserid settings

SITE_URL = 'http://quoteb.in/'
