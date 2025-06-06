# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalRootModel, update_forward_refs
from .foo import Foo

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def foo_1(self, value: Foo) -> UnionWithDuplicateTypes:
        if IS_PYDANTIC_V2:
            return UnionWithDuplicateTypes(
                root=_UnionWithDuplicateTypes.Foo1(**value.dict(exclude_unset=True), type="foo1")
            )  # type: ignore
        else:
            return UnionWithDuplicateTypes(
                __root__=_UnionWithDuplicateTypes.Foo1(**value.dict(exclude_unset=True), type="foo1")
            )  # type: ignore

    def foo_2(self, value: Foo) -> UnionWithDuplicateTypes:
        if IS_PYDANTIC_V2:
            return UnionWithDuplicateTypes(
                root=_UnionWithDuplicateTypes.Foo2(**value.dict(exclude_unset=True), type="foo2")
            )  # type: ignore
        else:
            return UnionWithDuplicateTypes(
                __root__=_UnionWithDuplicateTypes.Foo2(**value.dict(exclude_unset=True), type="foo2")
            )  # type: ignore


class UnionWithDuplicateTypes(UniversalRootModel):
    """
    Examples
    --------
    from seed.unions.resources.types import UnionWithDuplicateTypes_Foo1
    UnionWithDuplicateTypes_Foo1(name='example1', )
    """

    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[_UnionWithDuplicateTypes.Foo1, _UnionWithDuplicateTypes.Foo2],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(self) -> typing.Union[_UnionWithDuplicateTypes.Foo1, _UnionWithDuplicateTypes.Foo2]:
            return self.root
    else:
        __root__: typing_extensions.Annotated[
            typing.Union[_UnionWithDuplicateTypes.Foo1, _UnionWithDuplicateTypes.Foo2],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(self) -> typing.Union[_UnionWithDuplicateTypes.Foo1, _UnionWithDuplicateTypes.Foo2]:
            return self.__root__

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        if IS_PYDANTIC_V2:
            return self.root.dict(**kwargs)
        else:
            return self.__root__.dict(**kwargs)

    def visit(self, foo_1: typing.Callable[[Foo], T_Result], foo_2: typing.Callable[[Foo], T_Result]) -> T_Result:
        unioned_value = self.get_as_union()
        if unioned_value.type == "foo1":
            return foo_1(Foo(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "foo2":
            return foo_2(Foo(**unioned_value.dict(exclude_unset=True, exclude={"type"})))


class _UnionWithDuplicateTypes:
    class Foo1(Foo):
        type: typing.Literal["foo1"] = "foo1"

    class Foo2(Foo):
        type: typing.Literal["foo2"] = "foo2"


update_forward_refs(UnionWithDuplicateTypes)
