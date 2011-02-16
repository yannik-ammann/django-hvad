# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import connection
from nani.test_utils.context_managers import LanguageOverride
from nani.test_utils.data import DOUBLE_NORMAL
from nani.test_utils.testcase import NaniTestCase
from testproject.app.models import Normal


class FilterTests(NaniTestCase):
    fixtures = ['double_normal.json']
    
    def test_simple_filter(self):
        qs = Normal.objects.language('en').filter(shared_field__contains='2')
        self.assertEqual(qs.count(), 1)
        obj = qs[0]
        self.assertEqual(obj.shared_field, DOUBLE_NORMAL[2]['shared_field'])
        self.assertEqual(obj.translated_field, DOUBLE_NORMAL[2]['translated_field_en'])
        qs = Normal.objects.language('ja').filter(shared_field__contains='1')
        self.assertEqual(qs.count(), 1)
        obj = qs[0]
        self.assertEqual(obj.shared_field, DOUBLE_NORMAL[1]['shared_field'])
        self.assertEqual(obj.translated_field, DOUBLE_NORMAL[1]['translated_field_ja'])
        
    def test_translated_filter(self):
        qs = Normal.objects.filter(translated_field__contains='English')
        self.assertEqual(qs.count(), 2)
        obj1, obj2 = qs
        self.assertEqual(obj1.shared_field, DOUBLE_NORMAL[1]['shared_field'])
        self.assertEqual(obj1.translated_field, DOUBLE_NORMAL[1]['translated_field_en'])
        self.assertEqual(obj2.shared_field, DOUBLE_NORMAL[2]['shared_field'])
        self.assertEqual(obj2.translated_field, DOUBLE_NORMAL[2]['translated_field_en'])


class IterTests(NaniTestCase):
    fixtures = ['double_normal.json']
    
    def test_simple_iter(self):
        with LanguageOverride('en'):
            with self.assertNumQueries(1):
                index = 0
                for obj in Normal.objects.language():
                    index += 1
                    self.assertEqual(obj.shared_field, DOUBLE_NORMAL[index]['shared_field'])
                    self.assertEqual(obj.translated_field, DOUBLE_NORMAL[index]['translated_field_en'])
        with LanguageOverride('ja'):
            with self.assertNumQueries(1):
                index = 0
                for obj in Normal.objects.language():
                    index += 1
                    self.assertEqual(obj.shared_field, DOUBLE_NORMAL[index]['shared_field'])
                    self.assertEqual(obj.translated_field, DOUBLE_NORMAL[index]['translated_field_ja'])