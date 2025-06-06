# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..commons.types.language import Language
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions


class RawSyspropClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def set_num_warm_instances(
        self, language: Language, num_warm_instances: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        language : Language

        num_warm_instances : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sysprop/num-warm-instances/{jsonable_encoder(language)}/{jsonable_encoder(num_warm_instances)}",
            method="PUT",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return HttpResponse(response=_response, data=None)
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_num_warm_instances(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[Language, int]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[Language, int]]
        """
        _response = self._client_wrapper.httpx_client.request(
            "sysprop/num-warm-instances",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                typing.Dict[Language, int],
                parse_obj_as(
                    type_=typing.Dict[Language, int],  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSyspropClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def set_num_warm_instances(
        self, language: Language, num_warm_instances: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        language : Language

        num_warm_instances : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sysprop/num-warm-instances/{jsonable_encoder(language)}/{jsonable_encoder(num_warm_instances)}",
            method="PUT",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return AsyncHttpResponse(response=_response, data=None)
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_num_warm_instances(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[Language, int]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[Language, int]]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sysprop/num-warm-instances",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                typing.Dict[Language, int],
                parse_obj_as(
                    type_=typing.Dict[Language, int],  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
