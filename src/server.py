from contextlib import asynccontextmanager

from src.config.database import create_db_and_tables, get_session
from src.models.manutencao_model import Manutencao
from src.routes.manutencao_routes import manutencao_router

from fastapi import FastAPI

# Executa quando o FastAPI é iniciado
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(manutencao_router)

@app.get("/healthcheck")
def health_check():
    return {"status": "ok"}


