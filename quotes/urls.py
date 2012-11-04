from django.conf.urls import patterns, include, url

urlpatterns = patterns('quotes.views',
    url('^$', 'landing', name='landing'),
    url('^quotes/create/$', 'create_quote', name='create_quote'),
)
