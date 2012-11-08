from django.conf.urls import patterns, include, url

urlpatterns = patterns('quotes.views',
    url('^$', 'landing', name='landing'),
    url('^create/$', 'create_quote', name='create_quote'),
    url('^edit/(.+)/$', 'edit_quote', name='edit_quote'),
    url('^list/$', 'list_quotes', name='list_quotes'),
)
