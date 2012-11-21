from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response

from quotes.api.serializers import AuthorSerializer
from quotes.api.serializers import QuoteSerializer
from quotes.api.serializers import SourceSerializer
from quotes.models import Quote

class AuthorDetail(RetrieveAPIView):
    model = AuthorSerializer.Meta.model

    serializer_class = AuthorSerializer

class QuoteDetail(RetrieveAPIView):
    queryset = Quote.objects.filter(public=True)

    serializer_class = QuoteSerializer

class QuoteList(ListAPIView):
    queryset = Quote.objects.filter(public=True)

    serializer_class = QuoteSerializer

class SourceDetail(RetrieveAPIView):
    model = SourceSerializer.Meta.model

    serializer_class = SourceSerializer

@api_view(('GET',))
def root(request, format=None):
    return Response({
        'quotes': reverse('api.list_quotes', request=request),
    })

author = AuthorDetail.as_view()

list_quotes = QuoteList.as_view()

quote = QuoteDetail.as_view()

source = SourceDetail.as_view()
