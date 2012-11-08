from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from quotes.models import Quote
from quotes.forms import QuoteForm

def landing(request):
    return HttpResponse('Hi')

def _create_or_edit_quote(request, quote=None):
    form = QuoteForm(request, request.POST or None, instance=quote)

    if form.is_valid():
        quote = form.save()

        return redirect(reverse('landing'))

    return render(request, 'create_quote.html', {
        'form': form, 
    })

def create_quote(request):
    return _create_or_edit_quote(request)

def edit_quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id, user=request.user)

    return _create_or_edit_quote(request, quote=quote)
