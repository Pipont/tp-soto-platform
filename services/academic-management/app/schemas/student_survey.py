from pydantic import BaseModel
from typing import Optional

class StudentSurveyBase(BaseModel):
    repeat: Optional[int]
    misssc: Optional[int]
    skipping: Optional[int]
    tardysd: Optional[int]
    exerprac: Optional[int]
    studyhmw: Optional[int]
    workpay: Optional[int]
    workhome: Optional[int]

    st034q01ta: Optional[int]
    st034q02ta: Optional[int]
    st034q03ta: Optional[int]
    st034q04ta: Optional[int]
    st034q05ta: Optional[int]
    st034q06ta: Optional[int]

    st300q01ja: Optional[int]
    st300q02ja: Optional[int]
    st300q03ja: Optional[int]
    st300q04ja: Optional[int]
    st300q05ja: Optional[int]
    st300q06ja: Optional[int]
    st300q07ja: Optional[int]
    st300q08ja: Optional[int]
    st300q09ja: Optional[int]
    st300q10ja: Optional[int]

    st270q01ja: Optional[int]
    st270q02ja: Optional[int]
    st270q03ja: Optional[int]
    st270q04ja: Optional[int]

    st038q03na: Optional[int]
    st038q04na: Optional[int]
    st038q05na: Optional[int]
    st038q06na: Optional[int]
    st038q07na: Optional[int]
    st038q08na: Optional[int]

    st250q01ja: Optional[int]
    st250q02ja: Optional[int]
    st250q03ja: Optional[int]
    st250q04ja: Optional[int]
    st250q05ja: Optional[int]
    st251q01ja: Optional[int]
    st251q02ja: Optional[int]
    st251q03ja: Optional[int]
    st251q04ja: Optional[int]
    st255q01ja: Optional[int]

class StudentSurveyCreate(StudentSurveyBase):
    student_id: int

class StudentSurveyUpdate(StudentSurveyBase):
    pass

class StudentSurveyOut(StudentSurveyBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True
