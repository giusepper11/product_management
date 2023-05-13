import re
from typing import Optional
from pydantic import BaseModel, validator


class Category(BaseModel):
    id: Optional[int]
    name: str
    slug: str

    @validator("slug")
    def validate_slug(cls, raw_slug):
        if not re.match("^([a-z]|-|_)+$", raw_slug):
            raise ValueError("Invalid Slug")
        return raw_slug

    class Config:
        orm_mode = True
