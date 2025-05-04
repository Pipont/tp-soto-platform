from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.school import School, SchoolCreate
from app.crud import school as crud_school

router = APIRouter(prefix="/schools", tags=["schools"])

@router.post("/", response_model=School)
def create_school(school: SchoolCreate, db: Session = Depends(get_db)):
    return crud_school.create_school(db=db, school=school)

@router.get("/", response_model=list[School])
def read_schools(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_school.get_schools(db=db, skip=skip, limit=limit)

@router.get("/{school_id}", response_model=School)
def read_school(school_id: int, db: Session = Depends(get_db)):
    db_school = crud_school.get_school(db=db, school_id=school_id)
    if db_school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return db_school
