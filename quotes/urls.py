from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('quotes.views',
    url('^$', 'landing', name='landing'),
    url('^quotes/add/$', 'create_quote', name='create_quote'),
    url('^quotes/edit/(.+)/$', 'edit_quote', name='edit_quote'),
    url('^quotes/$', 'list_quotes', name='list_quotes'),

    url('^about/$', 'about', name='about'),
    url('^home/$', 'home', name='home'),

    url('^log-in/$', 'log_in', name='log_in'),
    url('^log-out/$', 'log_out', name='log_out'),
)
