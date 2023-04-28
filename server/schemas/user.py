from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel, validator, Field


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int


class UserDB(User):
    password_hash: str
    reg_date: datetime


class UserInfo(User):
    reg_date: datetime
    games_count: Optional[int] = 0
    max_score: Optional[int] = 0
    play_time: Optional[int] = 0

    @validator('*', pre=True)  # noqa, classmethod
    @classmethod
    def not_none(cls, value: Any, field: Field) -> Any:
        if all((getattr(field, 'default', None) is not None, value is None)):
            return field.default
        return value
