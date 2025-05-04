from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database import Base

class MathAssessment(Base):
    __tablename__ = "math_assessments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    math_cantidad = Column(Float)
    math_cambio_rel = Column(Float)
    math_espacio_forma = Column(Float)
    math_datos_incert = Column(Float)
    math_formulacion = Column(Float)
    math_procedimientos = Column(Float)
    math_interpretacion = Column(Float)
    math_razonamiento = Column(Float)
    math_promedio = Column(Float)
    math_logro = Column(Integer)