"""
Imports
"""
from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    """ Form test cases """
    def test_item_name_is_required(self):
        """ Failure - Instantiate without name provided """
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """ Success - Done field is not required """
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """ Success - only Name and Done fields specified on Form """
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
