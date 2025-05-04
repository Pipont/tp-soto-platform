from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.student_survey import StudentSurveyCreate, StudentSurveyOut
from app.crud import student_survey as crud

router = APIRouter(prefix="/student-surveys", tags=["student-surveys"])

@router.post("/", response_model=StudentSurveyOut)
def create(survey: StudentSurveyCreate, db: Session = Depends(get_db)):
    return crud.create_survey(db, survey)

@router.get("/", response_model=list[StudentSurveyOut])
def get_all(db: Session = Depends(get_db)):
    return crud.get_surveys(db)

@router.get("/student/{student_id}", response_model=StudentSurveyOut)
def get_by_student(student_id: int, db: Session = Depends(get_db)):
    survey = crud.get_survey_by_student(db, student_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Encuesta no encontrada")
    return survey
