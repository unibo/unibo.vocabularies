# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from unibo.vocabularies.testing import UNIBO_VOCABULARIES_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that unibo.vocabularies is properly installed."""

    layer = UNIBO_VOCABULARIES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if unibo.vocabularies is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'unibo.vocabularies'))

    def test_browserlayer(self):
        """Test that IUniboVocabulariesLayer is registered."""
        from unibo.vocabularies.interfaces import (
            IUniboVocabulariesLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IUniboVocabulariesLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = UNIBO_VOCABULARIES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['unibo.vocabularies'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if unibo.vocabularies is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'unibo.vocabularies'))

    def test_browserlayer_removed(self):
        """Test that IUniboVocabulariesLayer is removed."""
        from unibo.vocabularies.interfaces import \
            IUniboVocabulariesLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IUniboVocabulariesLayer,
            utils.registered_layers())
