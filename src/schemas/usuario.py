from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    cpf: str
    endereco: str