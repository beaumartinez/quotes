from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from quotes.models import Quote
from quotes.forms import DeleteQuoteForm
from quotes.forms import QuoteForm

def landing(request):
    if request.user.is_authenticated():
        return redirect(reverse('home'))

    return redirect(reverse('about'))

@login_required
def home(request):
    quotes = Quote.objects.filter(user=request.user.pk)

    return render(request, 'home.html', {
        'quotes': quotes,   
    })

def about(request):
    return render(request, 'about.html')

def _create_or_edit_quote(request, edit=False, quote=None):
    form_class = DeleteQuoteForm if edit else QuoteForm
    form = form_class(request, request.POST or None, instance=quote)

    if form.is_valid():
        quote = form.save()

        return redirect(reverse('landing'))

    return render(request, 'create_quote.html', {
        'edit': edit,
        'form': form, 
    })

@login_required
def create_quote(request):
    return _create_or_edit_quote(request)

@login_required
def edit_quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id, user=request.user.pk)

    return _create_or_edit_quote(request, edit=True, quote=quote)

@login_required
def list_quotes(request):
    quotes = Quote.objects.filter(user=request.user.pk)

    return render(request, 'list_quotes.html', {
        'quotes': quotes, 
    })

def log_in(request):
    return render(request, 'log_in.html')

def log_out(request):
    return logout_then_login(request, reverse('landing'))
