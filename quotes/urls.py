from django.conf.urls import patterns, include, url

urlpatterns = patterns('quotes.views',
    url('^$', 'landing', name='landing'),
    url('^create/$', 'create_quote', name='create_quote'),
    url('^edit/(.+)/$', 'edit_quote', name='edit_quote'),
    url('^list/$', 'list_quotes', name='list_quotes'),

    url('^about/$', 'about', name='about'),
    url('^home/$', 'home', name='home'),

    url('^log-in/$', 'log_in', name='log_in'),
    url('^log-out/$', 'log_out', name='log_out'),
)

urlpatterns += patterns('',
    url(r'^api/', include('quotes.api.urls', namespace='api')),
)

urlpatterns += patterns('',
    url(r'^browserid/', include('django_browserid.urls')),
)
