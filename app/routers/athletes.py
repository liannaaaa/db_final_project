from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix="/athletes")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_athlete(data: schemas.AthleteCreate, db: Session = Depends(get_db)):
    return crud.create_athlete(db, data)


@router.get("")
def list_athletes(
    limit: int = 10,
    offset: int = 0,
    sort: str = "id",
    db: Session = Depends(get_db)
):
    return crud.get_athletes(db, limit, offset, sort)


@router.post("/increment-wins")
def increment(country: str, db: Session = Depends(get_db)):
    crud.increment_wins_for_country(db, country)
    return {"status": "ok"}


@router.get("/group-by-country")
def group(db: Session = Depends(get_db)):
    return crud.group_by_country(db)


@router.get("/search")
def search(pattern: str, db: Session = Depends(get_db)):
    return crud.search_by_profile(db, pattern)
