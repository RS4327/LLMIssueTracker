
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / "src"))
print('Path ',sys.path.insert(0, str(BASE_DIR / "src")))

from fastapi import FastAPI

from LLMIssueTracker.API.routes import router

app = FastAPI(
    title="LLM Issue Tracker",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "Application": "LLM Issue Tracker"
    }