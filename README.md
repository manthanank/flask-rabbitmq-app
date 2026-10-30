# Flask RabbitMQ Application

A containerized application demonstrating message queuing between a Flask API (producer) and a consumer service using RabbitMQ.

## Project Structure

```text
flask-rabbitmq-app
├── .github/workflows    # CI/CD configuration
│   └── ci.yml          # GitHub Actions workflow
├── app/                 # Flask application
│   ├── __init__.py      # Flask app initialization
│   ├── consumer.py      # RabbitMQ message consumer
│   ├── producer.py      # Flask API for message production
│   └── rabbitmq.py      # RabbitMQ connection utilities
├── tests/               # Test suite
├── .gitignore           # Git ignore file
├── docker-compose.yml   # Docker Compose configuration
├── Dockerfile           # Docker image configuration
├── LICENSE              # Project license
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── run.py               # Application entry point
```

## Features

- RESTful API endpoint to send messages to RabbitMQ
- Separate consumer service for processing messages
- Docker containerization for easy deployment
- CI/CD pipeline with GitHub Actions

## Prerequisites

- Docker and Docker Compose
- Python 3.9+
- RabbitMQ (automatically provisioned via Docker)

## Getting Started

### Running with Docker Compose

1. Clone this repository
2. Start the application:

   ```bash
   docker-compose up -d
   ```

3. The Flask API will be available at <http://localhost:5000>

### Running Locally

1. Clone the repository and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start RabbitMQ (via Docker or local installation):

   ```bash
   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
   ```

3. Start the Flask application:

   ```bash
   python run.py
   ```

4. In a separate terminal, start the consumer:

   ```bash
   python -m app.consumer
   ```

## API Usage

Send a message to the queue:

```bash
curl -X POST http://localhost:5000/send \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello RabbitMQ!"}'
```

## Testing

Run the test suite:

```bash
pytest tests/
```

## Deployment

The project includes a GitHub Actions workflow that:

1. Runs tests on every push and pull request
2. Builds the Docker image
3. Validates the API is working correctly

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
