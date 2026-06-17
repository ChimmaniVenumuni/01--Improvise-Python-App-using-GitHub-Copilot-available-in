from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"


app = FastAPI(title="FastAPI Static + API Demo")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=FileResponse)
def root() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/hello")
def hello() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}
