from django.conf.urls import patterns, include, url

urlpatterns = patterns('quotes.views',
    url('^$', 'landing', name='landing'),
    url('^quotes/create/$', 'create_quote', name='create_quote'),
    url('^quotes/edit/(.+)$', 'edit_quote', name='edit_quote'),
    url('^quotes/list/$', 'list_quotes', name='list_quotes'),
)
