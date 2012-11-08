from re import sub

from django.forms import ModelForm
from django.forms import CharField

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from floppyforms.widgets import TextInput
from floppyforms.widgets import Textarea

from quotes.models import Author
from quotes.models import Quote
from quotes.models import Source

class QuoteForm(ModelForm):

    author = CharField(required=False, widget=TextInput(attrs={'placeholder': 'The quote\'s author. Optional'}))
    source = CharField(required=False, widget=TextInput(attrs={'placeholder': 'The quote\'s source. Optional'}))

    class Meta(object):
        model = Quote

        exclude = (
            'user',
        )

        widgets = {
            'content': Textarea(attrs={'placeholder': 'The quote. Required'}),
        }

    def __init__(self, request, *args, **kwargs):
        self.request = request

        super(QuoteForm, self).__init__(*args, **kwargs)

        # Set author name
        
        try:
            author_id = self.initial['author']
        except KeyError:
            pass
        else:
            try:
                author = Author.objects.get(pk=author_id)
            except Author.DoesNotExist:
                pass
            else:
                self.initial['author'] = author.name

        # Set source name

        try:
            source_id = self.initial['source']
        except KeyError:
            pass
        else:
            try:
                source = Source.objects.get(pk=source_id)
            except Source.DoesNotExist:
                pass
            else:
                self.initial['source'] = source.name

    def save(self, *args, **kwargs):
        commit = kwargs.pop('commit', True)

        kwargs['commit'] = False

        quote = super(QuoteForm, self).save(*args, **kwargs)
        quote.user = self.request.user

        if commit:
            quote.save()

        return quote

    def clean_author(self):
        author = self.data['author']
        author = author.strip()
        author = sub('\s+', ' ', author)

        if author != '':
            author, _ = Author.objects.get_or_create(name=author)
        else:
            author = None

        return author

    def clean_source(self):
        source = self.data['source']
        source = source.strip()
        source = sub('\s+', ' ', source)

        if source != '':
            source, _ = Source.objects.get_or_create(name=source)
        else:
            source = None

        return source

    helper = FormHelper()
    helper.layout = Layout(
        'content',
        'author',
        'source',

        FormActions(
            Submit('create', 'Create quote', css_class='btn-primary'),
        )
    )
