from django.core.urlresolvers import reverse_lazy

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

    # We put rest_framework down here to be able to override its templates
    'rest_framework',
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

STATIC_ROOT = 'static'

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

LOGIN_REDIRECT_URL = reverse_lazy('landing')
LOGIN_URL = reverse_lazy('log_in')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

# rest_framework settings

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

# Keys

try:
    from settings_keys import *
except ImportError:
    raise ValueError('Key settings (settings_keys.py) not found')

# Development settings

try:
    from settings_development import *
except ImportError:
    pass
