from pydantic import BaseModel


class RateCreate(BaseModel):
    game_score: int
    game_time: int


class RateRecord(RateCreate):
    line_number: int
    username: str
