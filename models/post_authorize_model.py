from pydantic import BaseModel


class PostRequestModel(BaseModel):
    name: str


class PostResponseModel(BaseModel):
    token: str
    user: str
