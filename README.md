# FastAPI Application
## Overview

This is a FastAPI application designed for managing Large Language Models (LLMs) and their performance metrics.
The application allows you to create LLMs, generate simulation data, and retrieve rankings based on various metrics.

## Features
- Create new LLM entries.
- Generate random simulation data for LLMs.
- Fetch rankings based on specified metrics.
- API key generation for secure access.

## Prerequisites

- Python 3.8 or higher
- PostgreSQL or another database configured with SQLAlchemy
- Redis (for message queuing, if applicable)
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the Repository:**
   cd your-repo-name
2.	Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Mac, On  Windows use `venv\Scripts\activate`
3.	Install Required Packages:
pip install -r requirements.txt
4.	Set Up Database:
o	Create a PostgreSQL database.
o	Configure the database connection in your environment or in a .env file.
Seed Initial Data (Optional):
You can optionally seed your database with initial data by running the seeding script:
python seed_data.py  # Adjust the filename as necessary
Running the Application
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


**CI/CD DEPLOYMWENT**
LLM Benchmark
Overview
LLM Benchmark is a Kubernetes-based application designed to evaluate and benchmark large language models (LLMs). 
This project leverages Helm for packaging and managing Kubernetes resources, making deployment and management straightforward.
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
Installation
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

