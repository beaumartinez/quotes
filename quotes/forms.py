from django.forms import ModelForm
from django.forms.widgets import TextInput

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit

from quotes.models import Author
from quotes.models import Quote
from quotes.models import Source

class QuoteForm(ModelForm):

    class Meta(object):
        model = Quote

        exclude = (
            'user',
        )

        widgets = {
            'author': TextInput,
            'source': TextInput,
        }

    def __init__(self, request, *args, **kwargs):
        self.request = request

        super(QuoteForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        commit = kwargs.pop('commit', True)

        kwargs['commit'] = False

        quote = super(QuoteForm, self).save(*args, **kwargs)
        quote.user = self.request.user

        if commit:
            quote.save()

        return quote

    helper = FormHelper()
    helper.layout = Layout(
        'content',
        'author',
        'source',

        FormActions(
            Submit('create', 'Create quote', css_class='btn-primary'),
        )
    )
