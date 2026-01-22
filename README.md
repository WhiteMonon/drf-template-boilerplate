# DRF Template Boilerplate

A minimal Django REST Framework (DRF) project template to kickstart APIs with sensible defaults for development, testing, and deployment.

## Features

- Django + Django REST Framework
- Token / JWT authentication scaffold (configurable)
- Docker & docker-compose support (optional)
- Example app structure (apps, serializers, views, urls)
- Preconfigured settings for local development and testing
- Basic test setup

## Tech stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL (recommended for production)
- Docker (optional)

## Quickstart

Requirements:
- Python 3.10+
- pip
- (optional) Docker & docker-compose

1. Clone
```bash
git clone https://github.com/WhiteMonon/drf-template-boilerplate.git
cd drf-template-boilerplate
```

2. Create virtual environment and install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Configuration

Create a `.env` file or set environment variables. Example `.env`:
```
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

4. Database & migrations
```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Run server
```bash
python manage.py runserver
```

## Docker (optional)

Build and start with docker-compose:
```bash
docker-compose up --build
```

## Tests

Run tests with:
```bash
pytest
```

or
```bash
python manage.py test
```

## API examples (Python)

Obtain an auth token (example uses `requests`):
```python
import requests

BASE = "http://localhost:8000"
resp = requests.post(f"{BASE}/api/auth/token/", data={
    "username": "admin",
    "password": "password"
})
print(resp.status_code, resp.json())
```

Call a protected endpoint:
```python
token = "your-token-here"
headers = {"Authorization": f"Bearer {token}"}
resp = requests.get(f"{BASE}/api/example/", headers=headers)
print(resp.json())
```

## Project structure (example)
- config/ — Django project settings
- apps/ — reusable Django apps
- requirements.txt
- Dockerfile / docker-compose.yml

## Contributing

Feel free to open issues or PRs. Keep changes small and add tests for new features.

## License

MIT License
