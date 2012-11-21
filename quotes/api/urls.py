from django.conf.urls import patterns, include, url

urlpatterns = patterns('quotes.api.views',
    url(r'^$', 'root', name='api.root'),

    url(r'^quotes/$', 'list_quotes', name='api.list_quotes'),
    url(r'^authors/$', 'list_authors', name='api.list_authors'),
    url(r'^sources/$', 'list_sources', name='api.list_sources'),

    url(r'^quotes/(?P<pk>.+)/$', 'quote', name='api.quote'),
    url(r'^authors/(?P<pk>.+)/$', 'author', name='api.author'),
    url(r'^sources/(?P<pk>.+)/$', 'source', name='api.source'),
)
