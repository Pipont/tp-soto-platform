import pika
import json

# Conexión a RabbitMQ (usa 'localhost' si corres desde tu máquina)

credentials = pika.PlainCredentials('user','password')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='student_prediction')

# Datos con todas las columnas requeridas, EXCEPTO la variable objetivo
message = {
    'PV1MATH': 480, 'PV2MATH': 475, 'PV3MATH': 500, 'PV4MATH': 500, 'PV5MATH': 495,
    'PV6MATH': 488, 'PV7MATH': 470, 'PV8MATH': 485, 'PV9MATH': 498, 'PV10MATH': 492,
    'AGE': 15, 'TFGender': 1,
    'REPEAT': 0, 'MISSSC': 0, 'SKIPPING': 0, 'TARDYSD': 0,
    'EXERPRAC': 2, 'STUDYHMW': 3, 'WORKPAY': 0, 'WORKHOME': 0,
    'ST034Q01TA': 4, 'ST034Q02TA': 4, 'ST034Q03TA': 3, 'ST034Q04TA': 3, 'ST034Q05TA': 3, 'ST034Q06TA': 4,
    'ST300Q01JA': 2, 'ST300Q02JA': 2, 'ST300Q03JA': 2, 'ST300Q04JA': 3, 'ST300Q05JA': 3,
    'ST300Q06JA': 2, 'ST300Q07JA': 3, 'ST300Q08JA': 3, 'ST300Q09JA': 4, 'ST300Q10JA': 3,
    'ST270Q01JA': 3, 'ST270Q02JA': 3, 'ST270Q03JA': 3, 'ST270Q04JA': 3,
    'ST038Q03NA': 1, 'ST038Q04NA': 2, 'ST038Q05NA': 1, 'ST038Q06NA': 1, 'ST038Q07NA': 1, 'ST038Q08NA': 1,
    'ST250Q01JA': 2, 'ST250Q02JA': 2, 'ST250Q03JA': 3, 'ST250Q04JA': 2, 'ST250Q05JA': 1,
    'ST251Q01JA': 3, 'ST251Q02JA': 2, 'ST251Q03JA': 3, 'ST251Q04JA': 1, 'ST255Q01JA': 2,
    'MATH_CANTIDAD': 500, 'MATH_CAMBIO_REL': 420, 'MATH_ESPACIO_FORMA': 490,
    'MATH_DATOS_INCERT': 250, 'MATH_FORMULACION': 350,
    'MATH_PROCEDIMIENTOS': 485, 'MATH_INTERPRETACION': 500, 'MATH_RAZONAMIENTO': 650,
    'MATH_PROMEDIO': 487
}


channel.basic_publish(
    exchange='',
    routing_key='student_prediction',
    body=json.dumps(message)
)

print("✅ Mensaje enviado correctamente.")
connection.close()
