from sqlalchemy import Column, Integer, String
from src.models.usuario import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id_categoria = Column(Integer, primary_key=True, index=True)
    nome_categoria = Column(String(50), nullable=False)