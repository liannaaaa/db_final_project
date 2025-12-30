from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix="/sport-types")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_sport_type(data: schemas.SportTypeCreate, db: Session = Depends(get_db)):
    return crud.create_sport_type(db, data)
