# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...core.request_options import RequestOptions
from ...core.http_response import HttpResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper
from ...core.http_response import AsyncHttpResponse
# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)
class RawParamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
    
    def get_with_path(self, param: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        GET with path param
        
        Parameters
        ----------
        param : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[str]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"params/path/{jsonable_encoder(param)}",method="GET",
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_ =str,  # type: ignore
                        object_ =_response.json()
                    )
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    def get_with_inline_path(self, param: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        GET with path param
        
        Parameters
        ----------
        param : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[str]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"params/path/{jsonable_encoder(param)}",method="GET",
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_ =str,  # type: ignore
                        object_ =_response.json()
                    )
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    def get_with_query(self, *, query: str, number: int, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        GET with query param
        
        Parameters
        ----------
        query : str
        
        number : int
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "params",method="GET",
            params={"query": query, "number": number, }
            ,
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    def get_with_allow_multiple_query(self, *, query: typing.Union[str, typing.Sequence[str]], number: typing.Union[int, typing.Sequence[int]], request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        GET with multiple of same query param
        
        Parameters
        ----------
        query : typing.Union[str, typing.Sequence[str]]
        
        number : typing.Union[int, typing.Sequence[int]]
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "params",method="GET",
            params={"query": query, "number": number, }
            ,
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    def get_with_path_and_query(self, param: str, *, query: str, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        GET with path and query params
        
        Parameters
        ----------
        param : str
        
        query : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"params/path-query/{jsonable_encoder(param)}",method="GET",
            params={"query": query, }
            ,
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    def get_with_inline_path_and_query(self, param: str, *, query: str, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        GET with path and query params
        
        Parameters
        ----------
        param : str
        
        query : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"params/path-query/{jsonable_encoder(param)}",method="GET",
            params={"query": query, }
            ,
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    def modify_with_path(self, param: str, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        PUT to update with path param
        
        Parameters
        ----------
        param : str
        
        request : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[str]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"params/path/{jsonable_encoder(param)}",method="PUT",
            json=request,
            request_options=request_options,omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_ =str,  # type: ignore
                        object_ =_response.json()
                    )
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    def modify_with_inline_path(self, param: str, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        PUT to update with path param
        
        Parameters
        ----------
        param : str
        
        request : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        HttpResponse[str]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"params/path/{jsonable_encoder(param)}",method="PUT",
            json=request,
            request_options=request_options,omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_ =str,  # type: ignore
                        object_ =_response.json()
                    )
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
class AsyncRawParamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
    
    async def get_with_path(self, param: str, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[str]:
        """
        GET with path param
        
        Parameters
        ----------
        param : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[str]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"params/path/{jsonable_encoder(param)}",method="GET",
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_ =str,  # type: ignore
                        object_ =_response.json()
                    )
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    async def get_with_inline_path(self, param: str, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[str]:
        """
        GET with path param
        
        Parameters
        ----------
        param : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[str]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"params/path/{jsonable_encoder(param)}",method="GET",
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_ =str,  # type: ignore
                        object_ =_response.json()
                    )
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    async def get_with_query(self, *, query: str, number: int, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        GET with query param
        
        Parameters
        ----------
        query : str
        
        number : int
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "params",method="GET",
            params={"query": query, "number": number, }
            ,
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    async def get_with_allow_multiple_query(self, *, query: typing.Union[str, typing.Sequence[str]], number: typing.Union[int, typing.Sequence[int]], request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        GET with multiple of same query param
        
        Parameters
        ----------
        query : typing.Union[str, typing.Sequence[str]]
        
        number : typing.Union[int, typing.Sequence[int]]
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "params",method="GET",
            params={"query": query, "number": number, }
            ,
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    async def get_with_path_and_query(self, param: str, *, query: str, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        GET with path and query params
        
        Parameters
        ----------
        param : str
        
        query : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"params/path-query/{jsonable_encoder(param)}",method="GET",
            params={"query": query, }
            ,
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    async def get_with_inline_path_and_query(self, param: str, *, query: str, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        GET with path and query params
        
        Parameters
        ----------
        param : str
        
        query : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"params/path-query/{jsonable_encoder(param)}",method="GET",
            params={"query": query, }
            ,
            request_options=request_options,)
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    async def modify_with_path(self, param: str, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[str]:
        """
        PUT to update with path param
        
        Parameters
        ----------
        param : str
        
        request : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[str]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"params/path/{jsonable_encoder(param)}",method="PUT",
            json=request,
            request_options=request_options,omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_ =str,  # type: ignore
                        object_ =_response.json()
                    )
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
    
    async def modify_with_inline_path(self, param: str, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[str]:
        """
        PUT to update with path param
        
        Parameters
        ----------
        param : str
        
        request : str
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        AsyncHttpResponse[str]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"params/path/{jsonable_encoder(param)}",method="PUT",
            json=request,
            request_options=request_options,omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_ =str,  # type: ignore
                        object_ =_response.json()
                    )
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
