from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('',
    url(r'', include('quotes.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^browserid/', include('django_browserid.urls')),
)
