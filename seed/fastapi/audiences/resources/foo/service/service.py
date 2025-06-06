# This file was auto-generated by Fern from our API Definition.

import abc
import functools
import inspect
import logging
import typing

import fastapi
from ....core.abstract_fern_service import AbstractFernService
from ....core.exceptions.fern_http_exception import FernHTTPException
from ....core.route_args import get_route_args
from ..types.importing_type import ImportingType
from .find_request import FindRequest


class AbstractFooService(AbstractFernService):
    """
    AbstractFooService is an abstract class containing the methods that you should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def find(self, *, body: FindRequest, optional_string: typing.Optional[str] = None) -> ImportingType: ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_find(router=router)

    @classmethod
    def __init_find(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.find)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "optional_string":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=..., alias="optionalString")))
            else:
                new_parameters.append(parameter)
        setattr(cls.find, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.find)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> ImportingType:
            try:
                return cls.find(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'find' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.find.__globals__)

        router.post(
            path="/",
            response_model=ImportingType,
            description=AbstractFooService.find.__doc__,
            **get_route_args(cls.find, default_tag="foo"),
        )(wrapper)
