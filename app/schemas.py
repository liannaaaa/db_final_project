from pydantic import BaseModel
from datetime import date


class SportTypeCreate(BaseModel):
    name: str
    unit: str | None = None
    world_record: float | None = None
    olympic_record: float | None = None


class AthleteCreate(BaseModel):
    full_name: str
    country: str | None = None
    birth_year: int | None = None
    wins_count: int | None = None


class ResultCreate(BaseModel):
    competition_name: str
    event_date: date
    event_place: str
    place: int
    result_value: float
    sport_type_id: int
    athlete_id: int
