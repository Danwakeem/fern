# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .optional_alias import OptionalAlias


class DoubleOptional(UniversalBaseModel):
    optional_alias: typing.Optional[OptionalAlias] = pydantic.Field(alias="optionalAlias", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.forbid
