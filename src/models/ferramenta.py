from sqlalchemy import Column, Integer, String, Boolean
# Importamos a Base que você já tinha criado no arquivo de usuário
from src.models.usuario import Base 

class Ferramenta(Base):
    __tablename__ = "tb_ferramentas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255))
    disponivel = Column(Boolean, default=True) # Começa sempre como disponível para aluguel