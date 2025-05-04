from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.student import StudentCreate, StudentOut
from app.crud import student as crud
from app.database import get_db

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/", response_model=StudentOut)
def create(student: StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.get("/", response_model=list[StudentOut])
def get_all(db: Session = Depends(get_db)):
    return crud.get_students(db)

@router.get("/{student_id}", response_model=StudentOut)
def get_by_id(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return student

@router.put("/{student_id}", response_model=StudentOut)
def update(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    updated = crud.update_student(db, student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return updated

@router.delete("/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db)):
    eliminado = crud.delete_student(db, student_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return {"ok": True, "mensaje": "Estudiante eliminado"}


@router.post("/students/{id}/predict")
def predict_student(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    survey = db.query(StudentSurvey).filter(StudentSurvey.student_id == id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Encuesta no encontrada")

    data = {**student.__dict__, **survey.__dict__}
    data.pop('_sa_instance_state', None)

    try:
        validate_and_send(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "🧠 Datos enviados para predicción correctamente"}
