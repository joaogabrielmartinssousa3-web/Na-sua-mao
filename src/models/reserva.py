from sqlalchemy import Column, Integer, DECIMAL, Date, Enum, TIMESTAMP, ForeignKey, text
from src.models.usuario import Base

class Reserva(Base):
    __tablename__ = "reservas"

    id_reserva = Column(Integer, primary_key=True, index=True)
    id_locatario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_ferramenta = Column(Integer, ForeignKey("ferramentas.id_ferramenta"), nullable=False)
    data_prevista_inicio = Column(Date, nullable=False)
    data_prevista_fim = Column(Date, nullable=False)
    valor_total_calculado = Column(DECIMAL(10,2), nullable=False)
    status_reserva = Column(Enum('Pendente', 'Confirmada', 'Cancelada', 'Finalizada'), server_default='Pendente')
    data_solicitacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))