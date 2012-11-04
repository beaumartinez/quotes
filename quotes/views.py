from django.http import HttpResponse
from django.shortcuts import render

from quotes.forms import QuoteForm

def landing(request):
    return HttpResponse('Hi')

def create_quote(request):
    form = QuoteForm(request.POST or None)

    if form.is_valid():
        quote = form.save()

    return render(request, 'create_quote.html', {
        'form': form, 
    })
