from fastapi import APIRouter
from sqlmodel import select

from src.config.database import get_session
from src.models.manutencao_model import Manutencao

manutencao_router = APIRouter(prefix="/manutencoes")


@manutencao_router.post("")
def criar_manutencao(manutencao: Manutencao):
    with get_session() as session:
        session.add(manutencao)
        session.commit()
        session.refresh(manutencao)
        return manutencao


@manutencao_router.get("/{id}")
def obter_manutencao_por_id(id: str):
    with get_session() as session:
        manutencao = session.exec(select(Manutencao).where(Manutencao.id == id))
        return manutencao
