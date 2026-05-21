from pydantic import BaseModel
from typing import Optional

class FerramentaCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None 
    disponivel: bool = True