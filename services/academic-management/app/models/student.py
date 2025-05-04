from sqlalchemy import Column, Integer, String, Date, Boolean
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_code = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date)
    gender = Column(String)  # Opcional: podrías mapear esto luego como 0 = F, 1 = M
    grade = Column(Integer)  # Grado en el colegio
    section = Column(String)
    is_active = Column(Boolean, default=True)
