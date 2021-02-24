from pydantic import Field, BaseModel


class User(BaseModel):
    username: str = Field(...)
