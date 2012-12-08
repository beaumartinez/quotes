from collections import Mapping
from collections import Sequence
from itertools import imap

from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.serializers import ManyHyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from quotes.models import Author
from quotes.models import Quote
from quotes.models import Source

def _filter_falsish_values(dict_):
    return {key: value for key, value in dict_.iteritems() if bool(value)}

class _NoNullFieldModelSerializer(ModelSerializer):

    # Remove null fields
    def convert_object(self, object_):
        converted = super(_NoNullFieldModelSerializer, self).convert_object(object_)
        converted = _filter_falsish_values(converted)

        return converted

    # Account for Author or Source being None and hence not having any fields
    def to_native(self, object_):
        try:
            return super(_NoNullFieldModelSerializer, self).to_native(object_)
        except AttributeError:
            return None

class SimpleAuthorSerializer(_NoNullFieldModelSerializer):

    url = HyperlinkedIdentityField(view_name='api.author')

    class Meta(object):
        model = Author

class SimpleSourceSerializer(_NoNullFieldModelSerializer):

    url = HyperlinkedIdentityField(view_name='api.source')

    class Meta(object):
        model = Source

class QuoteSerializer(_NoNullFieldModelSerializer):

    url = HyperlinkedIdentityField(view_name='api.quote')

    author = SimpleAuthorSerializer()
    source = SimpleSourceSerializer()

    class Meta(object):
        model = Quote

        exclude = (
            'user',
        )

class AuthorSerializer(SimpleAuthorSerializer):

    quotes = QuoteSerializer()

class SourceSerializer(SimpleSourceSerializer):

    quotes = QuoteSerializer()
