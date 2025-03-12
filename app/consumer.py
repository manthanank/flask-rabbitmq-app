import pika
from app.rabbitmq import get_rabbitmq_connection, declare_queue

def callback(ch, method, properties, body):
    """Process received message"""
    print(f"Received: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consumer():
    """Start RabbitMQ consumer"""
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    
    declare_queue(channel)  # Ensure queue exists

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    print("Waiting for messages...")
    channel.start_consuming()

if __name__ == '__main__':
    start_consumer()
