from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from .database import Base


class SportType(Base):
    __tablename__ = "sport_types"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit = Column(String)
    world_record = Column(Numeric)
    olympic_record = Column(Numeric)

    results = relationship("Result", back_populates="sport_type")


class Athlete(Base):
    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    country = Column(String)
    birth_year = Column(Integer)
    wins_count = Column(Integer)

    results = relationship("Result", back_populates="athlete")


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

    sport_type = relationship("SportType", back_populates="results")
    athlete = relationship("Athlete", back_populates="results")
