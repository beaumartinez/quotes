from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response

from quotes.api.serializers import AuthorSerializer
from quotes.api.serializers import QuoteSerializer
from quotes.api.serializers import SourceSerializer

class AuthorDetail(RetrieveAPIView):
    model = AuthorSerializer.Meta.model

    serializer_class = AuthorSerializer

class AuthorList(ListAPIView):
    model = AuthorSerializer.Meta.model

    serializer_class = AuthorSerializer

class QuoteDetail(RetrieveAPIView):
    model = QuoteSerializer.Meta.model

    serializer_class = QuoteSerializer

class QuoteList(ListAPIView):
    model = QuoteSerializer.Meta.model

    serializer_class = QuoteSerializer

class SourceDetail(RetrieveAPIView):
    model = SourceSerializer.Meta.model

    serializer_class = SourceSerializer

class SourceList(ListAPIView):
    model = SourceSerializer.Meta.model

    serializer_class = SourceSerializer

@api_view(('GET',))
def root(request, format=None):
    return Response({
        'authors': reverse('api.list_authors', request=request),
        'quotes': reverse('api.list_quotes', request=request),
        'sources': reverse('api.list_sources', request=request),
    })

author = AuthorDetail.as_view()

list_authors = AuthorList.as_view()

list_quotes = QuoteList.as_view()

list_sources = SourceList.as_view()

quote = QuoteDetail.as_view()

source = SourceDetail.as_view()
