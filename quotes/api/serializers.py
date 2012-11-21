from rest_framework.serializers import HyperlinkedIdentityField
from rest_framework.serializers import ManyHyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from quotes.models import Author
from quotes.models import Quote
from quotes.models import Source

class AuthorSerializer(ModelSerializer):

    class Meta(object):
        model = Author

    def to_native(self, object_):
        try:
            return super(AuthorSerializer, self).to_native(object_)
        except AttributeError:
            return None

    url = HyperlinkedIdentityField(view_name='api.author')
    quotes = ManyHyperlinkedRelatedField(view_name='api.quote')

class SourceSerializer(ModelSerializer):

    class Meta(object):
        model = Source

    def to_native(self, object_):
        try:
            return super(SourceSerializer, self).to_native(object_)
        except AttributeError:
            return None

    url = HyperlinkedIdentityField(view_name='api.source')
    quotes = ManyHyperlinkedRelatedField(view_name='api.quote')

class QuoteSerializer(ModelSerializer):

    class Meta(object):
        model = Quote

        exclude = (
            'public',
            'user',
        )

    url = HyperlinkedIdentityField(view_name='api.quote')

    author = AuthorSerializer()
    source = SourceSerializer()
