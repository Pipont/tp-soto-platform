# 📋 Historias de Usuario – Plataforma de Predicción del Rendimiento Académico

Este documento reúne las historias de usuario necesarias para el desarrollo de la plataforma web orientada a instituciones educativas. La solución permite la gestión académica, el procesamiento de datos y la predicción automatizada del rendimiento escolar utilizando inteligencia artificial y arquitectura basada en microservicios.

---

## 🎯 Estructura de historia


---

## 🚦 Historias agrupadas por módulo

### 🔐 Autenticación y Acceso
- HU-001: Como docente, quiero iniciar sesión con usuario y contraseña para acceder a mis funcionalidades.
- HU-020: Como administrador, quiero gestionar usuarios (crear, editar, eliminar).
- HU-021: Como sistema, quiero validar que cada request contenga un JWT válido.

---

### 🌐 API Gateway
- HU-022: Como sistema, quiero enrutar las peticiones al microservicio correcto según el endpoint.
- HU-023: Como microservicio, quiero recibir el `id_colegio` para operar correctamente bajo multitenant.

---

### 🏫 Gestión Académica
- HU-003: Como docente, quiero registrar a nuevos estudiantes en mi aula.
- HU-004: Como docente, quiero ver la lista de alumnos con sus datos registrados.
- HU-005: Como docente, quiero registrar las notas por cada curso del alumno.
- HU-006: Como docente, quiero registrar la asistencia mensual de cada alumno.
- HU-007: Como docente, quiero modificar los datos de un alumno si hay errores.
- HU-008: Como docente, quiero eliminar un alumno de mi lista si se retira del colegio.
- HU-018: Como docente, quiero registrar comentarios sobre el desempeño de cada estudiante.
- HU-027: Como docente, quiero subir un archivo CSV con todos los datos de mis alumnos.

---

### ⚙️ Preprocesamiento y Envío a Modelo
- HU-009: Como sistema, quiero recibir los datos cargados y validarlos automáticamente.
- HU-010: Como sistema, quiero enviar los datos preprocesados a la cola de predicción.

---

### 🤖 Predicción (AI)
- HU-011: Como microservicio, quiero procesar los datos con el modelo predictivo entrenado.
- HU-012: Como microservicio, quiero enviar los resultados de la predicción a la cola de resultados.
- HU-028: Como sistema, quiero procesar los mensajes de predicción aunque lleguen en distinto orden.

---

### 📊 Resultados y Reportes
- HU-013: Como sistema, quiero recibir los resultados del modelo y almacenarlos en la base de datos.
- HU-014: Como docente, quiero visualizar la predicción de rendimiento por estudiante.
- HU-019: Como docente, quiero ver el historial de predicciones de un alumno.
- HU-030: Como alumno, quiero ver mi resultado de predicción al iniciar sesión.
- HU-017: Como director, quiero exportar un reporte PDF con los alumnos en riesgo.

---

### 🔔 Alertas y Paneles
- HU-015: Como docente, quiero recibir una alerta si un alumno está en riesgo de bajo rendimiento.
- HU-016: Como director, quiero ver un dashboard con el resumen de predicciones por grado.
- HU-029: Como director, quiero definir criterios de intervención académica según los niveles de riesgo.

---

### 🔍 Observabilidad y Control
- HU-024: Como sistema, quiero tener logs de las predicciones realizadas para auditoría.
- HU-025: Como administrador, quiero ver el estado de los microservicios desde un dashboard.
- HU-026: Como sistema, quiero registrar errores en una cola de Dead Letter si el modelo falla.

---

## 🗂️ Prioridades y sprints sugeridos

| ID      | Historia                                                                                 | Prioridad | Sprint |
|---------|------------------------------------------------------------------------------------------|-----------|--------|
| HU-001  | Inicio de sesión                                                                          | Alta      | 1      |
| HU-003  | Registro de alumnos                                                                       | Alta      | 1      |
| HU-004  | Consulta de alumnos                                                                       | Alta      | 1      |
| HU-005  | Registro de notas                                                                         | Alta      | 1      |
| HU-021  | Validación de JWT en API Gateway                                                         | Alta      | 1      |
| HU-022  | Enrutamiento interno                                                                      | Alta      | 1      |
| HU-006  | Registro de asistencia                                                                    | Alta      | 2      |
| HU-009  | Validación de datos antes de predecir                                                     | Alta      | 2      |
| HU-010  | Envío de datos a cola de predicción                                                       | Alta      | 2      |
| HU-023  | Soporte para multitenancy                                                                 | Alta      | 2      |
| HU-011  | Predicción con modelo                                                                     | Alta      | 3      |
| HU-012  | Envío del resultado a la cola                                                             | Alta      | 3      |
| HU-013  | Guardar resultados en la base                                                             | Alta      | 3      |
| HU-014  | Visualización de predicción                                                               | Alta      | 3      |
| HU-020  | Gestión de usuarios                                                                       | Alta      | 3      |
| HU-027  | Subida masiva de datos CSV                                                                | Alta      | 3      |
| HU-015  | Alertas por bajo rendimiento                                                              | Media     | 4      |
| HU-016  | Dashboard por grado                                                                       | Media     | 4      |
| HU-017  | Exportación de reporte PDF                                                                | Media     | 4      |
| HU-019  | Historial de predicciones                                                                 | Media     | 4      |
| HU-024  | Logs y trazabilidad                                                                       | Media     | 4      |
| HU-025  | Dashboard de estado de servicios                                                          | Media     | 4      |
| HU-007  | Edición de datos del alumno                                                               | Media     | 2      |
| HU-008  | Eliminación de alumno                                                                     | Media     | 2      |
| HU-026  | Manejo de errores con DLQ                                                                 | Media     | 4      |
| HU-018  | Comentarios por alumno                                                                    | Baja      | 4      |
| HU-028  | Procesamiento asincrónico ordenado                                                        | Alta      | 3      |
| HU-002  | Panel de inicio para docentes                                                             | Media     | 3      |
| HU-029  | Definición de niveles de intervención por director                                        | Baja      | 4      |
| HU-030  | Vista de predicción para estudiante                                                       | Baja      | 4      |

---

## 🔚 Consideraciones

Estas historias pueden dividirse en tareas técnicas más pequeñas (issues) y cada una debe tener:
- Criterios de aceptación
- Pruebas funcionales (si aplica)
- Revisión por pares

Este documento debe evolucionar con cada sprint de trabajo.

