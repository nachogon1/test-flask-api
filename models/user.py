from typing import List

from pydantic import Field, BaseModel

from models.base import Base


class UserRef(BaseModel):
    user_id: str


class UserModel(BaseModel):
    username: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    post_ids: List[str] = []
    # TODO: comment why scale bad these points ids and how I would solve it.


class User(Base, UserModel):
    pass
