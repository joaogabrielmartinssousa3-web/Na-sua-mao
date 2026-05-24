from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class FerramentaCreate(BaseModel):
    id_locador: int
    id_categoria: int
    titulo: str
    descricao: Optional[str] = None
    voltagem: str
    estado_conservacao: str
    preco_diaria: Decimal

class FerramentaResponse(BaseModel):
    id_ferramenta: int
    id_locador: int
    id_categoria: int
    titulo: str
    descricao: Optional[str] = None
    voltagem: str
    estado_conservacao: str
    preco_diaria: Decimal

    class Config:
        from_attributes = True