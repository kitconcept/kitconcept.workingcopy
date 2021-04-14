# -*- coding: utf-8 -*-
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.dexterity.fti import DexterityFTI
from kitconcept.workingcopy.behaviors.workingcopy import IWorkingCopy
from kitconcept.workingcopy.testing import WORKINGCOPY_CORE_INTEGRATION_TESTING  # noqa

import unittest


class TestWorkingCopyBlocksBehavior(unittest.TestCase):

    layer = WORKINGCOPY_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        login(self.portal, TEST_USER_NAME)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        fti = DexterityFTI("blocksfolder")
        self.portal.portal_types._setObject("blocksfolder", fti)
        fti.klass = "plone.dexterity.content.Container"
        fti.behaviors = ("kitconcept.workingcopy.WorkingCopy",)

    def test_basic_fields(self):
        self.portal.invokeFactory(
            "blocksfolder", id="blocksfolder", title=u"Folder with blocks"
        )

        self.portal["blocksfolder"].working_copy_blocks = {
            "uuid1": {"@type": "title"},
            "uuid2": {"@type": "description"},
        }

        self.portal["blocksfolder"].working_copy_blocks_layout = {
            "uuid1": {"@type": "title"},
            "uuid2": {"@type": "description"},
        }

    def test_behavior_provides(self):
        self.portal.invokeFactory(
            "blocksfolder", id="blocksfolder", title=u"Folder with blocks"
        )

        assert IWorkingCopy.providedBy(self.portal["blocksfolder"])
