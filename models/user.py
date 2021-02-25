from typing import List

from pydantic import Field, BaseModel


class UserModel(BaseModel):
    username: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    post_ids: List[int] = []
    # TODO: comment why scale bad these points ids and how I would solve it.


class User(BaseModel):
    id: int
