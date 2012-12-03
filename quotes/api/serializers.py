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
    filtered_dict = dict()

    for key, value in dict_.iteritems():
        if bool(value):
            new_value = value

            # Match any sequence apart from a string
            if isinstance(value, Sequence) and not isinstance(value, basestring):
                new_value = imap(lambda x: _filter_falsish_values(x), value)
            elif isinstance(value, Mapping):
                new_value = _filter_falsish_values(value)

            filtered_dict[key] = new_value

    return filtered_dict

class _NoNullFieldModelSerializer(ModelSerializer):

    @property
    def data(self):
        data = super(_NoNullFieldModelSerializer, self).data

        if isinstance(data, Sequence):
            data = imap(lambda x: _filter_falsish_values(x), data)
        else:
            data = _filter_falsish_values(data)

        return data

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
            'public',
            'user',
        )

class AuthorSerializer(SimpleAuthorSerializer):

    quotes = QuoteSerializer()

class SourceSerializer(SimpleSourceSerializer):

    quotes = QuoteSerializer()
