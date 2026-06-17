# Project Documentation

## Overview
This project is a FastAPI web application that:
- Serves a static landing page at `/`
- Exposes a sample API endpoint at `/api/hello`

The landing page uses a modern dark theme with:
- Centered card layout
- Rounded corners and soft shadows
- Styled action buttons
- A floating rocket symbol below the welcome name

## Tech Stack
- Python 3.12+
- FastAPI
- Uvicorn
- HTML + CSS (served from `static/`)

## Project Structure
- `main.py`: FastAPI app entrypoint and route definitions
- `requirements.txt`: Python dependencies
- `static/index.html`: Landing page markup
- `static/styles.css`: Landing page styles

## Local Setup
### 1. Create and activate virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## Run the App
Use the correct import path (`main:app`):
```bash
uvicorn main:app --reload
```

App URLs:
- Landing page: http://127.0.0.1:8000/
- API endpoint: http://127.0.0.1:8000/api/hello

## API Reference
### GET /api/hello
Returns a sample JSON response.

Example response:
```json
{
  "message": "Hello from FastAPI!"
}
```

## UI Notes
The landing page currently includes:
- Welcome title updated to "Chimmani Venumuni"
- Rocket symbol centered below the name
- Steve Jobs quote section
- Buttons: "Try it out" and "Project source"

## Common Issue
If you run this command:
```bash
uvicorn app:app --reload
```
you will get an import error because there is no `app.py` module.

Use:
```bash
uvicorn main:app --reload
```

## Optional Enhancements
- Add automated tests with `pytest`
- Add formatting/linting with `black` and `ruff`
- Add Docker support (`Dockerfile` + `docker-compose.yml`)
- Add CI workflow for lint and test checks
