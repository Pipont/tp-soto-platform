from pydantic import BaseModel
from datetime import date
from typing import Optional

class StudentBase(BaseModel):
    student_code: str
    first_name: str
    last_name: str
    birth_date: Optional[date]
    gender: Optional[str]
    grade: Optional[int]
    section: Optional[str]
    is_active: Optional[bool] = True

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int

    class Config:
        orm_mode = True
