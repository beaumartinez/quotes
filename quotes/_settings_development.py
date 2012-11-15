DEBUG = True
TEMPLATE_DEBUG = DEBUG

# rest_framework settings

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}

# django_browserid settings

SITE_URL = 'http://127.0.0.1:8000/'
