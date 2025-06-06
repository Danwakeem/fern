# This file was auto-generated by Fern from our API Definition.

import json
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.regular_response import RegularResponse
from .types.stream_response import StreamResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawDummyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @typing.overload
    def generate(
        self, *, stream: typing.Literal[True], num_events: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Iterator[StreamResponse]]:
        """
        Parameters
        ----------
        stream : typing.Literal[True]

        num_events : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        """
        ...

    @typing.overload
    def generate(
        self, *, stream: typing.Literal[False], num_events: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RegularResponse]:
        """
        Parameters
        ----------
        stream : typing.Literal[False]

        num_events : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        """
        ...

    def generate(
        self, *, stream: bool, num_events: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Union[typing.Iterator[StreamResponse], RegularResponse]]:
        """
        Parameters
        ----------
        stream : bool

        num_events : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        """
        _request_json = {
            "stream": stream,
            "num_events": num_events,
        }
        if stream:

            async def stream_generator():
                with self._client_wrapper.httpx_client.stream(
                    "generate",
                    method="POST",
                    json=_request_json,
                    request_options=request_options,
                    omit=OMIT,
                ) as _response:

                    def _stream() -> HttpResponse[
                        typing.Iterator[typing.Union[typing.Iterator[StreamResponse], RegularResponse]]
                    ]:
                        try:
                            if 200 <= _response.status_code < 300:

                                def _iter():
                                    for _text in _response.iter_lines():
                                        try:
                                            if len(_text) == 0:
                                                continue
                                            yield typing.cast(
                                                StreamResponse,
                                                parse_obj_as(
                                                    type_=StreamResponse,  # type: ignore
                                                    object_=json.loads(_text),
                                                ),
                                            )
                                        except Exception:
                                            pass
                                    return

                                return HttpResponse(response=_response, data=_iter())
                            _response.read()
                            _response_json = _response.json()
                        except JSONDecodeError:
                            raise ApiError(
                                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                            )
                        raise ApiError(
                            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
                        )

                    yield _stream()

            return stream_generator()
        else:
            _response = self._client_wrapper.httpx_client.request(
                "generate",
                method="POST",
                json=_request_json,
                request_options=request_options,
                omit=OMIT,
            )
            try:
                if 200 <= _response.status_code < 300:
                    _data = typing.cast(
                        RegularResponse,
                        parse_obj_as(
                            type_=RegularResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                    return HttpResponse(response=_response, data=_data)
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDummyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @typing.overload
    async def generate(
        self, *, stream: typing.Literal[True], num_events: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.AsyncIterator[StreamResponse]]:
        """
        Parameters
        ----------
        stream : typing.Literal[True]

        num_events : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        """
        ...

    @typing.overload
    async def generate(
        self, *, stream: typing.Literal[False], num_events: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RegularResponse]:
        """
        Parameters
        ----------
        stream : typing.Literal[False]

        num_events : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        """
        ...

    async def generate(
        self, *, stream: bool, num_events: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Union[typing.AsyncIterator[StreamResponse], RegularResponse]]:
        """
        Parameters
        ----------
        stream : bool

        num_events : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        """
        _request_json = {
            "stream": stream,
            "num_events": num_events,
        }
        if stream:

            async def stream_generator():
                async with self._client_wrapper.httpx_client.stream(
                    "generate",
                    method="POST",
                    json=_request_json,
                    request_options=request_options,
                    omit=OMIT,
                ) as _response:

                    async def _stream() -> AsyncHttpResponse[
                        typing.AsyncIterator[typing.Union[typing.AsyncIterator[StreamResponse], RegularResponse]]
                    ]:
                        try:
                            if 200 <= _response.status_code < 300:

                                async def _iter():
                                    async for _text in _response.aiter_lines():
                                        try:
                                            if len(_text) == 0:
                                                continue
                                            yield typing.cast(
                                                StreamResponse,
                                                parse_obj_as(
                                                    type_=StreamResponse,  # type: ignore
                                                    object_=json.loads(_text),
                                                ),
                                            )
                                        except Exception:
                                            pass
                                    return

                                return AsyncHttpResponse(response=_response, data=_iter())
                            await _response.aread()
                            _response_json = _response.json()
                        except JSONDecodeError:
                            raise ApiError(
                                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                            )
                        raise ApiError(
                            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
                        )

                    yield await _stream()

            return stream_generator()
        else:
            _response = await self._client_wrapper.httpx_client.request(
                "generate",
                method="POST",
                json=_request_json,
                request_options=request_options,
                omit=OMIT,
            )
            try:
                if 200 <= _response.status_code < 300:
                    _data = typing.cast(
                        RegularResponse,
                        parse_obj_as(
                            type_=RegularResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                    return AsyncHttpResponse(response=_response, data=_data)
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
