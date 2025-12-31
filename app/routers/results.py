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


@router.get("/join")
def join_results(db: Session = Depends(get_db)):
    return crud.join_results(db)
