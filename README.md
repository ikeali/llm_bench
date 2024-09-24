# FastAPI Application
## Overview

Overview
This is a FastAPI application designed for managing Large Language Models (LLMs) and their performance metrics. The application provides an API to create LLMs, generate simulation data, and retrieve rankings based on various metrics.

In addition, the project uses a frontend (React, Vue, or similar), Redis for caching and task queuing, and Celery for handling background tasks like data simulation and ranking computation.

# Features
Create new LLM entries.
Generate random simulation data for LLMs.
Fetch rankings based on specified metrics.
Frontend dashboard for visualizing LLM data and rankings.
Background tasks using Celery for handling intensive computations asynchronously.
API key generation for secure access.
Prerequisites
Backend: Python 3.8 or higher
Frontend: Node.js 14 or higher
Database: PostgreSQL
Message Queue: Redis (for task queuing with Celery)
Required Python packages (listed in requirements.txt)
Docker and Docker Compose (for containerized development)
Installation
Backend
Clone the Repository:


git clone https://github.com/your-repo-name.git
cd your-repo-name
Set Up a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Required Packages:


pip install -r requirements.txt
Set Up Database:

Create a PostgreSQL database.
Configure the database connection in your .env file or environment variables.
Set Up Redis:

Install and start Redis locally or configure the Redis server URL in your .env file.
Set Up Celery Worker: Celery will be responsible for background tasks such as data simulation or ranking computations. To start the worker:



celery -A app.celery_app worker --loglevel=info
Run the Application:



uvicorn main:app --reload
The app will be accessible at http://127.0.0.1:8000.
Frontend
Navigate to the Frontend Directory:



cd frontend
Install Frontend Dependencies:



npm install
Run the Frontend:



npm start
The frontend will be accessible at http://localhost:3000.
Docker Setup
To simplify the deployment and running of both the backend and frontend, you can use Docker:

Build and Run Docker Containers: Ensure your docker-compose.yml is configured properly. To start the services:



docker-compose up --build
Access the Application:

Backend: http://localhost:8000
Frontend: http://localhost:3000
Configuration
Ensure you have the following environment variables configured in your .env file for both local development and production:



DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database>
REDIS_URL=redis://<host>:<port>
CELERY_BROKER_URL=redis://<host>:<port>/0
CELERY_RESULT_BACKEND=redis://<host>:<port>/0
API Endpoints
Create LLM
Endpoint: POST /llms/
Request Body:
json

{
  "name": "LLM Name",
  "description": "Description of the LLM"
}
Generate API Key
Endpoint: POST /api-keys/
Request Body:
json

{
  "user_id": 1
}
Fetch Rankings
Endpoint: GET /rankings/
Query Parameters:
metric_identifier: The name or ID of the metric for which to fetch rankings.
Frontend Dashboard
The application provides a frontend dashboard for visualizing LLM data and performance metrics.

Features:
Dashboard: Displays various metrics and rankings for the LLMs.
Data Visualization: Graphical representation of LLM metrics using charts (e.g., line charts, bar charts, etc.).
Responsive UI: The dashboard is responsive and works across devices.

Background Task Processing (Celery + Redis)
To handle intensive tasks such as generating large amounts of simulation data or computing rankings, the project uses Celery with a Redis broker.

Start the Celery Worker:

celery -A app.celery_app worker --loglevel=info
Start Redis: Ensure Redis is running locally or in Docker. You can use Docker Compose to start Redis alongside the application.

Executing Background Tasks: When tasks such as generating simulations are triggered, they will be queued in Redis and processed by Celery workers in the background.

7. Running the Application
To run the FastAPI application, use the following command:
uvicorn main:app --reload
•	The app will be accessible at http://127.0.0.1:8000.
API Endpoints
Create LLM
•	Endpoint: POST /llms/
•	Request Body:
json
{
  "name": "LLM Name",
  "description": "Description of the LLM"
}
Generate API Key
•	Endpoint: POST /api-keys/
•	Request Body:
json
{
  "user_id": 1
}



Response:
json
{
  "api_key": "your_generated_api_key"
}
Fetch Rankings
•	Endpoint: GET /rankings/
•	Query Parameters:
o	metric_identifier: The name or ID of the metric for which to fetch rankings.

## Frontend
Navigate to the Frontend Directory:

cd frontend
Install Frontend Dependencies:

npm install
Run the Frontend:

npm start
The frontend will be accessible at http://localhost:3000.

**CI/CD DEPLOYMWENT**

This project can be deployed using Kubernetes for production environments. The Helm chart simplifies deploying the application into a Kubernetes cluster.

Table of Contents
•	Features
•	Prerequisites
•	Installation
•	Usage
•	Configuration
•	Testing
•	Contributing
•	License
Features
•	Deploys a configurable environment for benchmarking LLMs.
•	Supports customizable resource allocation.
•	Integrates with various metrics and monitoring tools.
•	Easy installation and upgrades using Helm.
Prerequisites
Before you begin, ensure you have the following installed:
•	Docker
•	Kubernetes
•	Helm
•	kubectl

cd llm_benchmark
1.	Install the Helm chart:
helm install llm-benchmark ./llm_benchmark
2.	Verify the installation:
kubectl get all -l app.kubernetes.io/instance=llm-benchmark
Usage
Once the application is deployed, you can access it via the exposed services. Use the following command to get the service details:
kubectl get svc llm-benchmark
Replace llm-benchmark with the actual service name if necessary.
Configuration
You can customize the deployment by modifying the values.yaml file. Here are some of the configurable parameters:
yaml
service:
  enabled: true
  port: 80
  type: ClusterIP

replicaCount: 3

image:
  repository: nginx
  tag: latest
  pullPolicy: IfNotPresent

serviceAccount:
  create: true
  automount: true
Example Configuration
To set custom values during installation, use the --set flag:
helm install llm-benchmark ./llm_benchmark --set replicaCount=5 --set service.port=8080
Testing
You can run the connection test by creating a test pod:
kubectl run llm-benchmark-test --image=busybox --command -- wget llm-benchmark:80
