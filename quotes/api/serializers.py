from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedIdentityField

from quotes.models import Author
from quotes.models import Quote
from quotes.models import Source

class AuthorSerializer(ModelSerializer):

    class Meta(object):
        model = Author

        view_name = 'api:author'

    def to_native(self, object_):
        try:
            return super(AuthorSerializer, self).to_native(object_)
        except AttributeError:
            return None

    url = HyperlinkedIdentityField(view_name='api:author')

class SourceSerializer(ModelSerializer):

    class Meta(object):
        model = Source

        view_name = 'api:source'

    def to_native(self, object_):
        try:
            return super(SourceSerializer, self).to_native(object_)
        except AttributeError:
            return None

    url = HyperlinkedIdentityField(view_name='api:source')

class QuoteSerializer(ModelSerializer):

    class Meta(object):
        model = Quote

        view_name = 'api:quote'

        exclude = ('user',)

    url = HyperlinkedIdentityField(view_name='api:quote')

    author = AuthorSerializer()
    source = SourceSerializer()
