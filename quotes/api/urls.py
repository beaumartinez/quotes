from django.conf.urls import patterns, include, url

urlpatterns = patterns('quotes.api.views',
    url(r'^$', 'root', name='root'),

    url(r'^quotes/$', 'list_quotes', name='list_quotes'),

    url(r'^quotes/(?P<pk>.+)/$', 'quote', name='quote'),
    url(r'^authors/(?P<pk>.+)/$', 'author', name='author'),
    url(r'^sources/(?P<pk>.+)/$', 'source', name='source'),
)
