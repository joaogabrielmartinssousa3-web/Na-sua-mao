from sqlalchemy import Column, Integer, String, Boolean

from src.models.usuario import Base 

class Ferramenta(Base):
    __tablename__ = "tb_ferramentas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255))
    disponivel = Column(Boolean, default=True) 