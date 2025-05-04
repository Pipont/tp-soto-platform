from fastapi import FastAPI
from app.routers import student, student_survey, school, teacher, course, math_assessment
from app.database import Base, engine



app = FastAPI(title="Gestión Académica")

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Registrar rutas
app.include_router(student.router)
app.include_router(student_survey.router)
app.include_router(school.router)
app.include_router(teacher.router)
app.include_router(course.router)
app.include_router(math_assessment.router)

