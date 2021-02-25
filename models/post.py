from typing import List, Optional

from pydantic import Field
from pydantic.main import BaseModel

from models.user import User


class Comment(BaseModel):
    text: str


class PostModel(BaseModel):
    title: str
    description: str
    likes: List[int]
    comments: Optional[List[Comment]] = Field(default=None)


class Post(PostModel):
    id: int
