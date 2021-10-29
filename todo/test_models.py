"""
Imports
"""
from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    """ Model test cases """
    def test_done_defaults_to_false(self):
        """ Success """
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        """ Success """
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
