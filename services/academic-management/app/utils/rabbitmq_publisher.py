import pika
import json
import os

# Puedes cargar esta lista desde un archivo compartido si quieres mantenerlo dinámico
REQUIRED_COLUMNS = [
    'PV1MATH', 'PV2MATH', 'PV3MATH', 'PV4MATH', 'PV5MATH', 'PV6MATH',
    'PV7MATH', 'PV8MATH', 'PV9MATH', 'PV10MATH', 'AGE', 'TFGender',
    'REPEAT', 'MISSSC', 'SKIPPING', 'TARDYSD', 'EXERPRAC', 'STUDYHMW',
    'WORKPAY', 'WORKHOME', 'ST034Q01TA', 'ST034Q02TA', 'ST034Q03TA',
    'ST034Q04TA', 'ST034Q05TA', 'ST034Q06TA', 'ST300Q01JA', 'ST300Q02JA',
    'ST300Q03JA', 'ST300Q04JA', 'ST300Q05JA', 'ST300Q06JA', 'ST300Q07JA',
    'ST300Q08JA', 'ST300Q09JA', 'ST300Q10JA', 'ST270Q01JA', 'ST270Q02JA',
    'ST270Q03JA', 'ST270Q04JA', 'ST038Q03NA', 'ST038Q04NA', 'ST038Q05NA',
    'ST038Q06NA', 'ST038Q07NA', 'ST038Q08NA', 'ST250Q01JA', 'ST250Q02JA',
    'ST250Q03JA', 'ST250Q04JA', 'ST250Q05JA', 'ST251Q01JA', 'ST251Q02JA',
    'ST251Q03JA', 'ST251Q04JA', 'ST255Q01JA', 'MATH_CANTIDAD',
    'MATH_CAMBIO_REL', 'MATH_ESPACIO_FORMA', 'MATH_DATOS_INCERT',
    'MATH_FORMULACION', 'MATH_PROCEDIMIENTOS', 'MATH_INTERPRETACION',
    'MATH_RAZONAMIENTO', 'MATH_PROMEDIO'
]

def validate_and_send(data):
    missing = [col for col in REQUIRED_COLUMNS if col not in data]
    if missing:
        raise ValueError(f"Faltan las siguientes columnas requeridas: {missing}")

    credentials = pika.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq', credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue='student_prediction', durable=True)

    message = json.dumps({k: data[k] for k in REQUIRED_COLUMNS})
    channel.basic_publish(
        exchange='',
        routing_key='student_prediction',
        body=message
    )
    connection.close()
