from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database import Base

class StudentSurvey(Base):
    __tablename__ = "student_surveys"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    # Actividad y contexto escolar
    repeat = Column(Integer)
    misssc = Column(Integer)
    skipping = Column(Integer)
    tardysd = Column(Integer)
    exerprac = Column(Integer)
    studyhmw = Column(Integer)
    workpay = Column(Integer)
    workhome = Column(Integer)

    # Pertenencia
    st034q01ta = Column(Integer)
    st034q02ta = Column(Integer)
    st034q03ta = Column(Integer)
    st034q04ta = Column(Integer)
    st034q05ta = Column(Integer)
    st034q06ta = Column(Integer)

    # Apoyo familiar
    st300q01ja = Column(Integer)
    st300q02ja = Column(Integer)
    st300q03ja = Column(Integer)
    st300q04ja = Column(Integer)
    st300q05ja = Column(Integer)
    st300q06ja = Column(Integer)
    st300q07ja = Column(Integer)
    st300q08ja = Column(Integer)
    st300q09ja = Column(Integer)
    st300q10ja = Column(Integer)

    # Apoyo docente
    st270q01ja = Column(Integer)
    st270q02ja = Column(Integer)
    st270q03ja = Column(Integer)
    st270q04ja = Column(Integer)

    # Bullying
    st038q03na = Column(Integer)
    st038q04na = Column(Integer)
    st038q05na = Column(Integer)
    st038q06na = Column(Integer)
    st038q07na = Column(Integer)
    st038q08na = Column(Integer)

    # Recursos del hogar
    st250q01ja = Column(Integer)
    st250q02ja = Column(Integer)
    st250q03ja = Column(Integer)
    st250q04ja = Column(Integer)
    st250q05ja = Column(Integer)
    st251q01ja = Column(Integer)
    st251q02ja = Column(Integer)
    st251q03ja = Column(Integer)
    st251q04ja = Column(Integer)
    st255q01ja = Column(Integer)
