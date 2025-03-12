import pika

def get_rabbitmq_connection():
    """Establish connection with RabbitMQ"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    return connection

def declare_queue(channel, queue_name="task_queue"):
    """Declare a durable queue"""
    channel.queue_declare(queue=queue_name, durable=True)
