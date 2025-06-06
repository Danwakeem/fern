# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ....commons.types.problem_id import ProblemId
from ....core.api_error import ApiError
from ....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ....core.http_response import AsyncHttpResponse, HttpResponse
from ....core.jsonable_encoder import jsonable_encoder
from ....core.pydantic_utilities import parse_obj_as
from ....core.request_options import RequestOptions
from .types.lightweight_problem_info_v_2 import LightweightProblemInfoV2
from .types.problem_info_v_2 import ProblemInfoV2


class RawProblemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_lightweight_problems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[LightweightProblemInfoV2]]:
        """
        Returns lightweight versions of all problems

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LightweightProblemInfoV2]]
        """
        _response = self._client_wrapper.httpx_client.request(
            "problems-v2/lightweight-problem-info",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                typing.List[LightweightProblemInfoV2],
                parse_obj_as(
                    type_=typing.List[LightweightProblemInfoV2],  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_problems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ProblemInfoV2]]:
        """
        Returns latest versions of all problems

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ProblemInfoV2]]
        """
        _response = self._client_wrapper.httpx_client.request(
            "problems-v2/problem-info",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                typing.List[ProblemInfoV2],
                parse_obj_as(
                    type_=typing.List[ProblemInfoV2],  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_latest_problem(
        self, problem_id: ProblemId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProblemInfoV2]:
        """
        Returns latest version of a problem

        Parameters
        ----------
        problem_id : ProblemId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProblemInfoV2]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"problems-v2/problem-info/{jsonable_encoder(problem_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ProblemInfoV2,
                parse_obj_as(
                    type_=ProblemInfoV2,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_problem_version(
        self, problem_id: ProblemId, problem_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProblemInfoV2]:
        """
        Returns requested version of a problem

        Parameters
        ----------
        problem_id : ProblemId

        problem_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProblemInfoV2]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"problems-v2/problem-info/{jsonable_encoder(problem_id)}/version/{jsonable_encoder(problem_version)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ProblemInfoV2,
                parse_obj_as(
                    type_=ProblemInfoV2,  # type: ignore
                    object_=_response_json,
                ),
            )
            return HttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawProblemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_lightweight_problems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[LightweightProblemInfoV2]]:
        """
        Returns lightweight versions of all problems

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LightweightProblemInfoV2]]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "problems-v2/lightweight-problem-info",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                typing.List[LightweightProblemInfoV2],
                parse_obj_as(
                    type_=typing.List[LightweightProblemInfoV2],  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_problems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ProblemInfoV2]]:
        """
        Returns latest versions of all problems

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ProblemInfoV2]]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "problems-v2/problem-info",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                typing.List[ProblemInfoV2],
                parse_obj_as(
                    type_=typing.List[ProblemInfoV2],  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_latest_problem(
        self, problem_id: ProblemId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProblemInfoV2]:
        """
        Returns latest version of a problem

        Parameters
        ----------
        problem_id : ProblemId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProblemInfoV2]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"problems-v2/problem-info/{jsonable_encoder(problem_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ProblemInfoV2,
                parse_obj_as(
                    type_=ProblemInfoV2,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_problem_version(
        self, problem_id: ProblemId, problem_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProblemInfoV2]:
        """
        Returns requested version of a problem

        Parameters
        ----------
        problem_id : ProblemId

        problem_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProblemInfoV2]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"problems-v2/problem-info/{jsonable_encoder(problem_id)}/version/{jsonable_encoder(problem_version)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        if 200 <= _response.status_code < 300:
            _data = typing.cast(
                ProblemInfoV2,
                parse_obj_as(
                    type_=ProblemInfoV2,  # type: ignore
                    object_=_response_json,
                ),
            )
            return AsyncHttpResponse(response=_response, data=_data)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
