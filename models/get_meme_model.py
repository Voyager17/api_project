from typing import List, Dict, Union, Optional

from pydantic import BaseModel


class Data(BaseModel):
    id: Optional[int] = None
    info: Optional[Dict[str, Union[List[str], str, int]]] = None
    tags: Optional[List[Union[str, int]]] = None
    text: Optional[str] = None
    updated_by: Optional[str] = None
    url: Optional[str] = None


class ResponseDataModel(BaseModel):
    data: List[Data]
