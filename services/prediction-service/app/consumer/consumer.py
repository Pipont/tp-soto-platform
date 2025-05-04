import pika
import json
import time
from app.model.predictor import predecir_rendimiento

def callback(ch, method, properties, body):
    data = json.loads(body)
    prediction = predecir_rendimiento(data)
    print("📊 Predicción realizada:", prediction)

def start_consuming():
    while True:
        try:
            credentials = pika.PlainCredentials('user','password')
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq',credentials=credentials)
            )
            break  # Solo sale si se logra conectar
        except pika.exceptions.AMQPConnectionError:
            print("⏳ Esperando que RabbitMQ esté disponible...")
            time.sleep(5)  # Espera 5 segundos antes de intentar de nuevo

    channel = connection.channel()
    channel.queue_declare(queue='student_prediction')

    channel.basic_consume(
        queue='student_prediction',
        on_message_callback=callback,
        auto_ack=True
    )

    print("📡 Esperando mensajes en la cola 'student_prediction'...")
    channel.start_consuming()

if __name__ == '__main__':
    start_consuming()
