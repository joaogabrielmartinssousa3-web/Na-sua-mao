from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Usuario(Base):
    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    

    cpf = Column(String(14), unique=True, nullable=False) 
    
    endereco = Column(String(255), nullable=False)
