from flask import Blueprint, request, jsonify
import pika
from app.rabbitmq import get_rabbitmq_connection, declare_queue

producer_bp = Blueprint('producer', __name__)

@producer_bp.route('/send', methods=['POST'])
def send_message():
    """Send message to RabbitMQ queue"""
    data = request.json
    message = data.get("message", "Hello, RabbitMQ!")

    connection = get_rabbitmq_connection()
    channel = connection.channel()
    
    declare_queue(channel)  # Ensure queue exists
    
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make message persistent
        )
    )

    connection.close()
    return jsonify({"message": "Sent successfully!"})
