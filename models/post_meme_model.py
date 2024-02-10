from typing import List, Dict, Union, Optional

from pydantic import BaseModel


class PostRequestModel(BaseModel):
    info: Dict[str, Union[List[str], str]]
    tags: List[str]
    text: str
    updated_by: Optional[str] = None
    url: str


class PostResponseModel(BaseModel):
    id: Optional[int] = None
    info: Optional[Dict[str, Union[List[str], str]]] = None
    tags: Optional[List[str]] = None
    text: Optional[str] = None
    updated_by: Optional[str] = None
    url: Optional[str] = None
