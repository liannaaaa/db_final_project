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
