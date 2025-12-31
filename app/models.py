from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from .database import Base


class SportType(Base):
    __tablename__ = "sport_types"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit = Column(String)
    world_record = Column(Numeric)
    olympic_record = Column(Numeric)


class Athlete(Base):
    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    country = Column(String)
    birth_year = Column(Integer)
    wins_count = Column(Integer, default=0)
    profile = Column(JSONB)


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True)
    competition_name = Column(String)
    event_date = Column(Date)
    event_place = Column(String)
    place = Column(Integer)
    result_value = Column(Numeric)

    sport_type_id = Column(Integer, ForeignKey("sport_types.id"))
    athlete_id = Column(Integer, ForeignKey("athletes.id"))

    athlete = relationship("Athlete")
    sport_type = relationship("SportType")
