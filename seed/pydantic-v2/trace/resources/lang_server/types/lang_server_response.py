from pydantic import BaseModel
from typing import Any
from dt import datetime
from core.datetime_utils import serialize_datetime
class LangServerResponse(BaseModel):
    response: Any
    class Config:
        frozen = True
        smart_union = True
        json_encoders = {datetime: serialize_datetime}

