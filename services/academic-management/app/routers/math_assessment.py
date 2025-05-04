# routers/math_assessment.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.math_assessment import MathAssessmentCreate, MathAssessmentOut
from app.crud.math_assessment import create_math_assessment, get_math_assessments, get_math_assessment_by_id

router = APIRouter(prefix="/math-assessments", tags=["Math Assessment"])

@router.post("/", response_model=MathAssessmentOut)
def create(data: MathAssessmentCreate, db: Session = Depends(get_db)):
    return create_math_assessment(db, data)

@router.get("/", response_model=list[MathAssessmentOut])
def list_all(db: Session = Depends(get_db)):
    return get_math_assessments(db)

@router.get("/{assessment_id}", response_model=MathAssessmentOut)
def get_by_id(assessment_id: int, db: Session = Depends(get_db)):
    assessment = get_math_assessment_by_id(db, assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Evaluación no encontrada")
    return assessment
