# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..types.with_cursor import WithCursor


class ListUsersBodyCursorPaginationRequest(UniversalBaseModel):
    pagination: typing.Optional[WithCursor] = pydantic.Field(default=None)
    """
    The object that contains the cursor used for pagination
    in order to fetch the next page of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="forbid")  # type: ignore # Pydantic v2
    else:

        class Config:
            extra = pydantic.Extra.forbid
