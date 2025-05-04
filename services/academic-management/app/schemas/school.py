from pydantic import BaseModel
from typing import Optional

class SchoolBase(BaseModel):
    name: str
    district: str
    region: str

class SchoolCreate(SchoolBase):
    pass

class School(SchoolBase):
    id: int

    class Config:
        orm_mode = True
