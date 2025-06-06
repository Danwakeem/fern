# This file was auto-generated by Fern from our API Definition.

import pydantic
from ......core.pydantic_utilities import UniversalBaseModel
from .object_with_optional_field import ObjectWithOptionalField


class NestedObjectWithRequiredField(UniversalBaseModel):
    string: str
    nested_object: ObjectWithOptionalField = pydantic.Field(alias="NestedObject")

    class Config:
        extra = pydantic.Extra.forbid
