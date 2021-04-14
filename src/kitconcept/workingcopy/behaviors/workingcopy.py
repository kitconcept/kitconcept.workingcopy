# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.restapi import _
from plone.schema import JSONField
from plone.supermodel import model
from zope.interface import provider

import json


WORKING_COPY_BLOCKS_SCHEMA = json.dumps({"type": "object", "properties": {}})

WORKING_COPY_LAYOUT_SCHEMA = json.dumps(
    {
        "type": "object",
        "properties": {"items": {"type": "array", "items": {"type": "string"}}},
    }
)


@provider(IFormFieldProvider)
class IWorkingCopy(model.Schema):

    model.fieldset(
        "working_copy",
        label=_(u"Working Copy"),
        fields=["working_copy_blocks", "working_copy_blocks_layout"],
    )

    working_copy_blocks = JSONField(
        title=u"Blocks",
        description=u"The JSON representation of the object blocks information. Must be a JSON object.",  # noqa
        schema=WORKING_COPY_BLOCKS_SCHEMA,
        default={},
        required=False,
    )

    working_copy_blocks_layout = JSONField(
        title=u"Blocks Layout",
        description=u"The JSON representation of the object blocks layout. Must be a JSON array.",  # noqa
        schema=WORKING_COPY_LAYOUT_SCHEMA,
        default={"items": []},
        required=False,
    )
