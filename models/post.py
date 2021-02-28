from datetime import datetime
from typing import List, Optional

from pydantic import Field, validator
from pydantic.main import BaseModel
from simpleflake import simpleflake, parse_simpleflake

from models.base import Base
from models.user import User, UserRef


class Comment(BaseModel):
    text: str
    author_id: str = None

class PostRef(BaseModel):
    post_id: str


class UserPostRef(UserRef, PostRef):
    pass


class PostModel(BaseModel):
    title: str
    description: str = None
    likes: List[str] = Field(default=[])
    comments: Optional[List[Comment]] = Field(default=[])




class Post(Base, PostModel):
    pass

