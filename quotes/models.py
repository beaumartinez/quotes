from django.contrib.auth.models import User
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import TextField

class Quote(Model):
    user = ForeignKey(User)

    content = TextField()
    author = ForeignKey('Author', null=True)
    source = ForeignKey('Source', null=True)

class Author(Model):
    name = CharField(max_length=100)

class Source(Model):
    name = CharField(max_length=100)
