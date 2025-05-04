from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    subject_area = Column(String)
    school_id = Column(Integer, ForeignKey("schools.id"))
