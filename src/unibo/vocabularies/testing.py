# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import unibo.vocabularies


class UniboVocabulariesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=unibo.vocabularies)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'unibo.vocabularies:default')


UNIBO_VOCABULARIES_FIXTURE = UniboVocabulariesLayer()


UNIBO_VOCABULARIES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UNIBO_VOCABULARIES_FIXTURE,),
    name='UniboVocabulariesLayer:IntegrationTesting',
)


UNIBO_VOCABULARIES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UNIBO_VOCABULARIES_FIXTURE,),
    name='UniboVocabulariesLayer:FunctionalTesting',
)


UNIBO_VOCABULARIES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        UNIBO_VOCABULARIES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='UniboVocabulariesLayer:AcceptanceTesting',
)
