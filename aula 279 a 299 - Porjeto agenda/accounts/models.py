from django.db import models
from contacts.models import Contact
from django import forms


class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('show',)
