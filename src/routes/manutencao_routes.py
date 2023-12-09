from fastapi import APIRouter
from fastapi.responses import JSONResponse
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
        manutencao = session.exec(select(Manutencao).where(Manutencao.id == id)).first()

        if not manutencao:
            return JSONResponse(
                status_code=404,
                content={
                    "message": f"Não foi encontrada uma manutenção com o id {id}",
                },
            )
        return manutencao


@manutencao_router.put("/{id}")
def modificar_manutencao_completa(id: str, manutencao_modificada: Manutencao):
    with get_session() as session:
        manutencao = session.exec(select(Manutencao).where(Manutencao.id == id)).first()

        if not manutencao:
            return JSONResponse(
                status_code=404,
                content={
                    "message": f"Não foi encontrada uma manutenção com o id {id}",
                },
            )

        for campo in manutencao.__fields__.keys():
            if campo == "id":
                continue
            valor_campo_mod = manutencao_modificada.__getattribute__(campo)
            manutencao.__setattr__(campo, valor_campo_mod)

        session.commit()
        session.refresh(manutencao)
        return manutencao


@manutencao_router.patch("/{id}")
def modificar_manutencao_parcial(id: str, manutencao_modificada: Manutencao):
    with get_session() as session:
        manutencao = session.exec(select(Manutencao).where(Manutencao.id == id)).first()

        if not manutencao:
            return JSONResponse(
                status_code=404,
                content={
                    "message": f"Não foi encontrada uma manutenção com o id {id}",
                },
            )

        for campo in manutencao_modificada.__fields__.keys():
            if campo == "id":
                continue

            valor_campo = manutencao.__getattribute__(campo)
            valor_campo_mod = manutencao_modificada.__getattribute__(campo)

            # Previne a atualização de um campo que não veio pela requisição
            if not valor_campo_mod:
                continue

            if valor_campo != valor_campo_mod:
                manutencao.__setattr__(campo, valor_campo_mod)

        session.commit()
        session.refresh(manutencao)
        return manutencao


@manutencao_router.delete("/{id}", status_code=204)
def excluir_manutencao(id: str):
    with get_session() as session:
        manutencao = session.exec(select(Manutencao).where(Manutencao.id == id)).first()

        if not manutencao:
            return JSONResponse(
                status_code=404,
                content={
                    "message": f"Não foi encontrada uma manutenção com o id {id}",
                },
            )
        session.delete(manutencao)

        session.commit()
        return None
