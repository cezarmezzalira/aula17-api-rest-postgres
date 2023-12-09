from typing import Optional
from sqlmodel import Field, SQLModel


class Manutencao(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    placa: str
    marca: str
    modelo: str
    cor: str
    nome_cliente: str
    nome_mecanico: str
    data_chegada: str
    data_finalizacao: Optional[str] = Field(default=None)