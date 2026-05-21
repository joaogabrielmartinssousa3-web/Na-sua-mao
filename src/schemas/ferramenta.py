from pydantic import BaseModel
from typing import Optional

class FerramentaCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None # A descrição é opcional
    disponivel: bool = True