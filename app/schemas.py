from pydantic import BaseModel
from typing import Optional, Dict
from datetime import date


class AthleteCreate(BaseModel):
    full_name: str
    country: Optional[str]
    birth_year: Optional[int]
    wins_count: Optional[int]
    profile: Optional[Dict]


class SportTypeCreate(BaseModel):
    name: str
    unit: Optional[str]
    world_record: Optional[float]
    olympic_record: Optional[float]


class ResultCreate(BaseModel):
    competition_name: str
    event_date: date
    event_place: str
    place: int
    result_value: float
    sport_type_id: int
    athlete_id: int
