from pydantic import BaseModel
from typing import Optional

class TeacherBase(BaseModel):
    name: str
    email: str
    subject_area: str
    school_id: int

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int

    class Config:
        orm_mode = True
