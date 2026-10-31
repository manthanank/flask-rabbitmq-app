from unittest.mock import MagicMock

import pytest
from app import create_app


@pytest.fixture
def client(monkeypatch):
    # Tests run without a RabbitMQ broker; stub out the connection.
    monkeypatch.setattr("app.producer.get_rabbitmq_connection", MagicMock())
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_send_message(client):
    response = client.post('/send', json={"message": "Test Message"})
    assert response.status_code == 200
    assert response.json["message"] == "Sent successfully!"