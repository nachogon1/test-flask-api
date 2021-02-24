from typing import List, Optional

from pydantic import Field
from pydantic.main import BaseModel

from models.user import User


class Comment(User):
    text: str


class Post(User):
    title: str
    description: str
    comments: Optional[List[Comment]] = Field(default=None)
