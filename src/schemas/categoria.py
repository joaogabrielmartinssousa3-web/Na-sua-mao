from pydantic import BaseModel

class CategoriaCreate(BaseModel):
    nome_categoria: str

class CategoriaResponse(BaseModel):
    id_categoria: int
    nome_categoria: str

    class Config:
        from_attributes = True