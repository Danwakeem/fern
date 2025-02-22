# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ..commons.problem_id import ProblemId
from .code_execution_update import CodeExecutionUpdate
from .exception_info import ExceptionInfo
from .terminated_response import TerminatedResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SubmissionResponse_ServerInitialized(pydantic.BaseModel):
    type: typing.Literal["serverInitialized"]


class SubmissionResponse_ProblemInitialized(pydantic.BaseModel):
    type: typing.Literal["problemInitialized"]
    value: ProblemId


class SubmissionResponse_WorkspaceInitialized(pydantic.BaseModel):
    type: typing.Literal["workspaceInitialized"]


class SubmissionResponse_ServerErrored(ExceptionInfo):
    type: typing.Literal["serverErrored"]

    class Config:
        allow_population_by_field_name = True


class SubmissionResponse_CodeExecutionUpdate(pydantic.BaseModel):
    type: typing.Literal["codeExecutionUpdate"]
    value: CodeExecutionUpdate


class SubmissionResponse_Terminated(TerminatedResponse):
    type: typing.Literal["terminated"]

    class Config:
        allow_population_by_field_name = True


SubmissionResponse = typing.Union[
    SubmissionResponse_ServerInitialized,
    SubmissionResponse_ProblemInitialized,
    SubmissionResponse_WorkspaceInitialized,
    SubmissionResponse_ServerErrored,
    SubmissionResponse_CodeExecutionUpdate,
    SubmissionResponse_Terminated,
]
