from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix="/results")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def create_result(data: schemas.ResultCreate, db: Session = Depends(get_db)):
    return crud.create_result(db, data)


@router.get("/by-country")
def results_by_country(country: str, db: Session = Depends(get_db)):
    return crud.get_results_by_country(db, country)
