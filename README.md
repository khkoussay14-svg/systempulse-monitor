# SystemPulse

SystemPulse is a lightweight system and network monitoring dashboard built with FastAPI. It exposes a small REST API and a browser dashboard for checking CPU, memory, disk and basic network information.

## Features

- CPU usage
- Memory usage
- Disk usage
- Hostname and operating system information
- Network interface addresses
- JSON REST endpoint
- Simple responsive dashboard
- Docker support
- Basic API test

## Tech stack

- Python 3.12
- FastAPI
- Uvicorn
- psutil
- HTML, CSS and JavaScript
- Pytest
- Docker

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://localhost:8000`.

## API

`GET /api/system`

Example response:

```json
{
  "hostname": "my-pc",
  "platform": "Linux",
  "cpu_percent": 12.5,
  "memory_percent": 43.2,
  "disk_percent": 61.4,
  "network": [
    {"interface": "eth0", "address": "192.168.1.10"}
  ]
}
```

## Run with Docker

```bash
docker build -t systempulse .
docker run --rm -p 8000:8000 systempulse
```

## Why this project

SystemPulse was created as a portfolio project to practice Python backend development, REST APIs, system/network concepts and containerization while keeping the codebase small enough to understand and explain clearly.
