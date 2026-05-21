from sqlalchemy import Column, Integer, String, DECIMAL, Enum, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    cep = Column(String(9), nullable=False)
    telefone = Column(String(15))
    reputacao_acumulada = Column(DECIMAL(3,2), server_default=text("5.00"))
    tipo_perfil = Column(Enum('Morador', 'Administrador'), server_default="Morador")
    data_cadastro = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))