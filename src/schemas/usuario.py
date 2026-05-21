from pydantic import BaseModel
from typing import Optional

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    cpf: str
    cep: str
    telefone: Optional[str] = None