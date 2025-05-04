from pydantic import BaseModel
from typing import Optional

class MathAssessmentBase(BaseModel):
    math_cantidad: float
    math_cambio_rel: float
    math_espacio_forma: float
    math_datos_incert: float
    math_formulacion: float
    math_procedimientos: float
    math_interpretacion: float
    math_razonamiento: float
    math_promedio: float
    math_logro: int

class MathAssessmentCreate(MathAssessmentBase):
    student_id: int
    


class MathAssessmentOut(MathAssessmentBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True