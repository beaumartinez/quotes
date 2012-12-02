from collections import Sequence
from itertools import imap

from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.serializers import ManyHyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from quotes.models import Author
from quotes.models import Quote
from quotes.models import Source

def _filter_none_values(dict_):
    return {key: value for key, value in dict_.iteritems() if value is not None}

class _NoNullFieldModelSerializer(ModelSerializer):

    @property
    def data(self):
        data = super(_NoNullFieldModelSerializer, self).data

        if isinstance(data, Sequence):
            data = imap(lambda x: _filter_none_values(x), data)
        else:
            data = _filter_none_values(data)

        return data

class AuthorSerializer(_NoNullFieldModelSerializer):

    class Meta(object):
        model = Author

    def to_native(self, object_):
        try:
            return super(AuthorSerializer, self).to_native(object_)
        except AttributeError:
            return None

    url = HyperlinkedIdentityField(view_name='api.author')
    quotes = ManyHyperlinkedRelatedField(view_name='api.quote')

class SourceSerializer(_NoNullFieldModelSerializer):

    class Meta(object):
        model = Source

    def to_native(self, object_):
        try:
            return super(SourceSerializer, self).to_native(object_)
        except AttributeError:
            return None

    url = HyperlinkedIdentityField(view_name='api.source')
    quotes = ManyHyperlinkedRelatedField(view_name='api.quote')

class QuoteSerializer(_NoNullFieldModelSerializer):

    class Meta(object):
        model = Quote

        exclude = (
            'public',
            'user',
        )

    url = HyperlinkedIdentityField(view_name='api.quote')

    author = AuthorSerializer()
    source = SourceSerializer()
