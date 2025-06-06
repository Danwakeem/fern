# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...core.pydantic_utilities import UniversalBaseModel


class UnionWithPrimitive_Integer(UniversalBaseModel):
    value: int
    type: typing.Literal["integer"] = "integer"


class UnionWithPrimitive_String(UniversalBaseModel):
    value: str
    type: typing.Literal["string"] = "string"


"""
from seed.unions.resources import UnionWithPrimitive_Integer

UnionWithPrimitive_Integer(value=9)
"""
UnionWithPrimitive = typing.Union[UnionWithPrimitive_Integer, UnionWithPrimitive_String]
