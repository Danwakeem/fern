# This file was auto-generated by Fern from our API Definition.

import abc
import functools
import inspect
import logging
import typing

import fastapi
from ......core.abstract_fern_service import AbstractFernService
from ......core.exceptions.fern_http_exception import FernHTTPException
from ......core.route_args import get_route_args
from ......security import ApiAuth, FernAuth
from .....types.resources.object.types.object_with_required_field import ObjectWithRequiredField


class AbstractEndpointsContainerService(AbstractFernService):
    """
    AbstractEndpointsContainerService is an abstract class containing the methods that you should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def get_and_return_list_of_primitives(self, *, body: typing.List[str], auth: ApiAuth) -> typing.Sequence[str]: ...

    @abc.abstractmethod
    def get_and_return_list_of_objects(
        self, *, body: typing.List[ObjectWithRequiredField], auth: ApiAuth
    ) -> typing.Sequence[ObjectWithRequiredField]: ...

    @abc.abstractmethod
    def get_and_return_set_of_primitives(self, *, body: typing.Set[str], auth: ApiAuth) -> typing.Set[str]: ...

    @abc.abstractmethod
    def get_and_return_set_of_objects(
        self, *, body: typing.List[ObjectWithRequiredField], auth: ApiAuth
    ) -> typing.Sequence[ObjectWithRequiredField]: ...

    @abc.abstractmethod
    def get_and_return_map_prim_to_prim(
        self, *, body: typing.Dict[str, str], auth: ApiAuth
    ) -> typing.Dict[str, str]: ...

    @abc.abstractmethod
    def get_and_return_map_of_prim_to_object(
        self, *, body: typing.Dict[str, ObjectWithRequiredField], auth: ApiAuth
    ) -> typing.Dict[str, ObjectWithRequiredField]: ...

    @abc.abstractmethod
    def get_and_return_optional(
        self, *, body: typing.Optional[ObjectWithRequiredField] = None, auth: ApiAuth
    ) -> typing.Optional[ObjectWithRequiredField]: ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_get_and_return_list_of_primitives(router=router)
        cls.__init_get_and_return_list_of_objects(router=router)
        cls.__init_get_and_return_set_of_primitives(router=router)
        cls.__init_get_and_return_set_of_objects(router=router)
        cls.__init_get_and_return_map_prim_to_prim(router=router)
        cls.__init_get_and_return_map_of_prim_to_object(router=router)
        cls.__init_get_and_return_optional(router=router)

    @classmethod
    def __init_get_and_return_list_of_primitives(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_and_return_list_of_primitives)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.get_and_return_list_of_primitives, "__signature__", endpoint_function.replace(parameters=new_parameters)
        )

        @functools.wraps(cls.get_and_return_list_of_primitives)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Sequence[str]:
            try:
                return cls.get_and_return_list_of_primitives(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_and_return_list_of_primitives' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_and_return_list_of_primitives.__globals__)

        router.post(
            path="/container/list-of-primitives",
            response_model=typing.Sequence[str],
            description=AbstractEndpointsContainerService.get_and_return_list_of_primitives.__doc__,
            **get_route_args(cls.get_and_return_list_of_primitives, default_tag="endpoints.container"),
        )(wrapper)

    @classmethod
    def __init_get_and_return_list_of_objects(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_and_return_list_of_objects)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.get_and_return_list_of_objects, "__signature__", endpoint_function.replace(parameters=new_parameters)
        )

        @functools.wraps(cls.get_and_return_list_of_objects)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Sequence[ObjectWithRequiredField]:
            try:
                return cls.get_and_return_list_of_objects(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_and_return_list_of_objects' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_and_return_list_of_objects.__globals__)

        router.post(
            path="/container/list-of-objects",
            response_model=typing.Sequence[ObjectWithRequiredField],
            description=AbstractEndpointsContainerService.get_and_return_list_of_objects.__doc__,
            **get_route_args(cls.get_and_return_list_of_objects, default_tag="endpoints.container"),
        )(wrapper)

    @classmethod
    def __init_get_and_return_set_of_primitives(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_and_return_set_of_primitives)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.get_and_return_set_of_primitives, "__signature__", endpoint_function.replace(parameters=new_parameters)
        )

        @functools.wraps(cls.get_and_return_set_of_primitives)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Set[str]:
            try:
                return cls.get_and_return_set_of_primitives(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_and_return_set_of_primitives' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_and_return_set_of_primitives.__globals__)

        router.post(
            path="/container/set-of-primitives",
            response_model=typing.Set[str],
            description=AbstractEndpointsContainerService.get_and_return_set_of_primitives.__doc__,
            **get_route_args(cls.get_and_return_set_of_primitives, default_tag="endpoints.container"),
        )(wrapper)

    @classmethod
    def __init_get_and_return_set_of_objects(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_and_return_set_of_objects)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.get_and_return_set_of_objects, "__signature__", endpoint_function.replace(parameters=new_parameters)
        )

        @functools.wraps(cls.get_and_return_set_of_objects)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Sequence[ObjectWithRequiredField]:
            try:
                return cls.get_and_return_set_of_objects(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_and_return_set_of_objects' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_and_return_set_of_objects.__globals__)

        router.post(
            path="/container/set-of-objects",
            response_model=typing.Sequence[ObjectWithRequiredField],
            description=AbstractEndpointsContainerService.get_and_return_set_of_objects.__doc__,
            **get_route_args(cls.get_and_return_set_of_objects, default_tag="endpoints.container"),
        )(wrapper)

    @classmethod
    def __init_get_and_return_map_prim_to_prim(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_and_return_map_prim_to_prim)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.get_and_return_map_prim_to_prim, "__signature__", endpoint_function.replace(parameters=new_parameters)
        )

        @functools.wraps(cls.get_and_return_map_prim_to_prim)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Dict[str, str]:
            try:
                return cls.get_and_return_map_prim_to_prim(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_and_return_map_prim_to_prim' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_and_return_map_prim_to_prim.__globals__)

        router.post(
            path="/container/map-prim-to-prim",
            response_model=typing.Dict[str, str],
            description=AbstractEndpointsContainerService.get_and_return_map_prim_to_prim.__doc__,
            **get_route_args(cls.get_and_return_map_prim_to_prim, default_tag="endpoints.container"),
        )(wrapper)

    @classmethod
    def __init_get_and_return_map_of_prim_to_object(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_and_return_map_of_prim_to_object)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.get_and_return_map_of_prim_to_object,
            "__signature__",
            endpoint_function.replace(parameters=new_parameters),
        )

        @functools.wraps(cls.get_and_return_map_of_prim_to_object)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Dict[str, ObjectWithRequiredField]:
            try:
                return cls.get_and_return_map_of_prim_to_object(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_and_return_map_of_prim_to_object' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_and_return_map_of_prim_to_object.__globals__)

        router.post(
            path="/container/map-prim-to-object",
            response_model=typing.Dict[str, ObjectWithRequiredField],
            description=AbstractEndpointsContainerService.get_and_return_map_of_prim_to_object.__doc__,
            **get_route_args(cls.get_and_return_map_of_prim_to_object, default_tag="endpoints.container"),
        )(wrapper)

    @classmethod
    def __init_get_and_return_optional(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_and_return_optional)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_and_return_optional, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_and_return_optional)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Optional[ObjectWithRequiredField]:
            try:
                return cls.get_and_return_optional(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_and_return_optional' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_and_return_optional.__globals__)

        router.post(
            path="/container/opt-objects",
            response_model=typing.Optional[ObjectWithRequiredField],
            description=AbstractEndpointsContainerService.get_and_return_optional.__doc__,
            **get_route_args(cls.get_and_return_optional, default_tag="endpoints.container"),
        )(wrapper)
