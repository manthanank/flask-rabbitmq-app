from flask import Flask
from app.producer import producer_bp

def create_app():
    """Create and configure the Flask app"""
    app = Flask(__name__)
    app.register_blueprint(producer_bp)

    return app
