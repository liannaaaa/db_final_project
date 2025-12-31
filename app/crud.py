from sqlalchemy.orm import Session
from sqlalchemy import text
from .models import Athlete, SportType, Result


def create_athlete(db: Session, data):
    obj = Athlete(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_sport_type(db: Session, data):
    obj = SportType(**data.dict())
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


def increment_wins_for_country(db: Session, country: str):
    db.execute(
        text("""
        UPDATE athletes
        SET wins_count = wins_count + 1
        WHERE country = :country
        """),
        {"country": country}
    )
    db.commit()

def group_by_country(db: Session):
    return db.execute(
        text("""
        SELECT country, COUNT(*) AS cnt
        FROM athletes
        GROUP BY country
        """)
    ).fetchall()

def join_results(db: Session):
    return db.execute(
        text("""
        SELECT a.full_name, s.name, r.result_value, r.place
        FROM results r
        JOIN athletes a ON a.id = r.athlete_id
        JOIN sport_types s ON s.id = r.sport_type_id
        """)
    ).fetchall()

def search_by_profile(db: Session, pattern: str):
    return db.execute(
        text("""
        SELECT * FROM athletes
        WHERE profile::text ~ :pattern
        """),
        {"pattern": pattern}
    ).fetchall()

def get_athletes(db: Session, limit: int, offset: int, sort: str):
    query = f"SELECT * FROM athletes ORDER BY {sort} LIMIT :limit OFFSET :offset"
    return db.execute(
        text(query),
        {"limit": limit, "offset": offset}
    ).fetchall()
