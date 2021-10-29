"""
Imports
"""
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """ Form class """
    class Meta:
        """ Meta class of form """
        model = Item
        fields = ['name', 'done']
