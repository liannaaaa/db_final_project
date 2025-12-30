from sqlalchemy.orm import Session
from .models import SportType, Athlete, Result


def create_sport_type(db: Session, data):
    obj = SportType(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def create_athlete(db: Session, data):
    obj = Athlete(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def create_result(db: Session, data):
    obj = Result(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_results_by_country(db: Session, country: str):
    return (
        db.query(Result)
        .join(Athlete)
        .filter(Athlete.country == country)
        .all()
    )
