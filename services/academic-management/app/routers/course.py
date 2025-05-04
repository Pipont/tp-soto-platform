from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.course import CourseCreate, CourseOut
from app.crud import course as crud

router = APIRouter(prefix="/courses", tags=["courses"])

@router.post("/", response_model=CourseOut)
def create(course: CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)

@router.get("/", response_model=list[CourseOut])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all_courses(db)

@router.get("/{course_id}", response_model=CourseOut)
def get_by_id(course_id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return course
