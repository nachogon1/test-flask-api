from datetime import datetime
from typing import Optional

from pydantic import validator
from pydantic.main import BaseModel
from simpleflake import simpleflake


class Base(BaseModel):
    id: Optional[str]
    created: datetime = datetime.utcnow()
    changed: Optional[datetime] = None

    @validator('id', pre=True, always=True)
    def always_id(cls, v, values):
        if v:
            return v
        else:
            return simpleflake()

    @validator('changed', always=True)
    def always_changed(cls, v, values):
        if not values.get("changed"):
            return values["created"]  # It would better to parse the timestamp.
