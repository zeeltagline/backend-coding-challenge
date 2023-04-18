from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI

from app.api.planning import router as planning_router

app = FastAPI()


# Load environment variables from .env file
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

app.include_router(planning_router, prefix="/planning", tags=["planning"])
