from pathlib import Path
import hashlib
import secrets
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
 
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
 
app = FastAPI(title="FastAPI Static + API Demo")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
 
# Step 1: Pydantic model for JSON body
class TextInput(BaseModel):
    text: str
 
# Existing/Helper generate function to create pseudo-random tokens
def generate(text: str) -> list[str]:
    """Generates pseudo-random tokens based on input text."""
    return [secrets.token_hex(8) for _ in range(3)]
 
@app.get("/", response_class=FileResponse)
def root() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")
 
# Step 3: Welcome note with participant name
@app.get("/api/hello")
def hello() -> dict[str, str]:
    """Returns a customized welcome message."""
    return {"message": "Hello from FastAPI! - Shaban Kaishar"}
 
# Step 2: POST endpoint accepting JSON body with 'text' and returning tokens + checksum
@app.post("/generate")
def generate_endpoint(payload: TextInput) -> dict:
    """
    Accepts a single field 'text' in JSON body,
    calls generate(), and returns tokens with a SHA-256 checksum.
    """
    tokens = generate(payload.text)
    checksum = hashlib.sha256(payload.text.encode()).hexdigest()
    return {
        "text": payload.text,
        "tokens": tokens,
        "checksum": checksum
    }
