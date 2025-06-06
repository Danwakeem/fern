# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .stack_frame import StackFrame


class StackInformation(UniversalBaseModel):
    num_stack_frames: int = pydantic.Field(alias="numStackFrames")
    top_stack_frame: typing.Optional[StackFrame] = pydantic.Field(alias="topStackFrame", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.allow


from ..commons.debug_key_value_pairs import DebugKeyValuePairs  # noqa: E402, F401, I001
from ..commons.debug_map_value import DebugMapValue  # noqa: E402, F401, I001

update_forward_refs(StackInformation)
