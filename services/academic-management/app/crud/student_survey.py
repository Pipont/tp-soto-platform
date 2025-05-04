from sqlalchemy.orm import Session
from app.models.student_survey import StudentSurvey
from app.schemas.student_survey import StudentSurveyCreate

def create_survey(db: Session, survey: StudentSurveyCreate):
    db_survey = StudentSurvey(**survey.dict())
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def get_surveys(db: Session):
    return db.query(StudentSurvey).all()

def get_survey_by_student(db: Session, student_id: int):
    return db.query(StudentSurvey).filter(StudentSurvey.student_id == student_id).first()
