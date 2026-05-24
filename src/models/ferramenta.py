from sqlalchemy import Column, Integer, String, Text, DECIMAL, Enum, ForeignKey
from src.models.usuario import Base 

class Ferramenta(Base):
    __tablename__ = "ferramentas" 

    id_ferramenta = Column(Integer, primary_key=True, index=True)
    id_locador = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"), nullable=False)
    titulo = Column(String(100), nullable=False)
    descricao = Column(Text)
    voltagem = Column(Enum('110v', '220v', 'Bivolt', 'Bateria'), nullable=False)
    estado_conservacao = Column(Enum('Novo', 'Excelente', 'Bom'), nullable=False)
    preco_diaria = Column(DECIMAL(10,2), nullable=False)
    status_ferramenta = Column(Enum('Disponível', 'Reservado', 'Em Uso', 'Em Manutenção'), server_default='Disponível')