from django import forms
from django.forms import ModelForm

from .models import Contact


class Contacte(ModelForm):
    class Meta():
        model = Contact
        fields = ['nom','prenom','email','sujet','messages']