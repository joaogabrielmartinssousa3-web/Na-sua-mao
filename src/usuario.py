from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Cria a base para as nossas tabelas
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    
    # O unique=True garante que não teremos CPFs duplicados (RN-011)
    cpf = Column(String(14), unique=True, nullable=False) 
    
    endereco = Column(String(255), nullable=False)