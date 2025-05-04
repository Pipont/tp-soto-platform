from sqlalchemy.orm import Session
from app.models.math_assessment import MathAssessment
from app.schemas.math_assessment import MathAssessmentCreate

def create_math_assessment(db: Session, assessment: MathAssessmentCreate):
    db_assessment = MathAssessment(**assessment.dict())
    db.add(db_assessment)
    db.commit()
    db.refresh(db_assessment)
    return db_assessment

def get_math_assessments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MathAssessment).offset(skip).limit(limit).all()

def get_math_assessment_by_id(db: Session, assessment_id: int):
    return db.query(MathAssessment).filter(MathAssessment.id == assessment_id).first()