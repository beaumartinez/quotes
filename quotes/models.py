from django.contrib.auth.models import User
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import TextField

class Quote(Model):
    user = ForeignKey(User)

    content = TextField()
    author = ForeignKey('Author', blank=True, null=True, related_name='quotes')
    source = ForeignKey('Source', blank=True, null=True, related_name='quotes')

    public = BooleanField(default=True)

class Author(Model):
    name = CharField(max_length=100, unique=True)

class Source(Model):
    name = CharField(max_length=100, unique=True)
