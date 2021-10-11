# -*- coding: utf-8 -*-
from unibo.vocabularies.testing import UNIBO_VOCABULARIES_INTEGRATION_TESTING  # noqa
from unibo.vocabularies.universities import italianUniversitiesVocabulary

import unittest


class TestUniversities(unittest.TestCase):
    """Test unibo.vocabularies."""

    layer = UNIBO_VOCABULARIES_INTEGRATION_TESTING

    def test_unibo(self):
        term = italianUniversitiesVocabulary.getTerm(3701)
        self.assertEqual(term.title, u'Universit\xe0 degli Studi di Bologna')
        self.assertEqual(term.token, '3701')
