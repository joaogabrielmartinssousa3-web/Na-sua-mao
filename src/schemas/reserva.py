from pydantic import BaseModel
from datetime import date, datetime
from decimal import Decimal
from typing import Optional

class ReservaCreate(BaseModel):
    id_locatario: int
    id_ferramenta: int
    data_prevista_inicio: date
    data_prevista_fim: date
    valor_total_calculado: Decimal

class ReservaResponse(BaseModel):
    id_reserva: int
    id_locatario: int
    id_ferramenta: int
    data_prevista_inicio: date
    data_prevista_fim: date
    valor_total_calculado: Decimal
    status_reserva: str
    data_solicitacao: Optional[datetime] = None

    class Config:
        from_attributes = True