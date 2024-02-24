from typing import Any
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar
from typing import Union

from pydantic import BaseModel

T = TypeVar("T")


# Response information
class Status(BaseModel):
    code: int = 200
    message: str


# Standard web response
class WebResponse(Generic[T], BaseModel):
    info: Status
    data: Optional[Union[List[T], T]] = None
