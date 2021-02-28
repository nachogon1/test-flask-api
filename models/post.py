from datetime import datetime
from typing import List, Optional

from pydantic import Field, validator
from pydantic.main import BaseModel
from simpleflake import simpleflake, parse_simpleflake

from models.base import Base
from models.user import User


class Comment(BaseModel):
    text: str
    author: int = None


class PostModel(BaseModel):
    title: str
    description: str = None
    likes: List[int] = Field(default=[])
    comments: Optional[List[Comment]] = Field(default=None)


class PostRef(BaseModel):
    post_id: int


class Post(Base, PostModel):
    pass

