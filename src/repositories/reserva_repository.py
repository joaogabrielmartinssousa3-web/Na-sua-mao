from sqlalchemy.orm import Session
from src.models.reserva import Reserva
from src.schemas.reserva import ReservaCreate

class ReservaRepository:
    def criar_reserva(self, db: Session, reserva: ReservaCreate):
        nova_reserva = Reserva(
            id_locatario=reserva.id_locatario,
            id_ferramenta=reserva.id_ferramenta,
            data_prevista_inicio=reserva.data_prevista_inicio,
            data_prevista_fim=reserva.data_prevista_fim,
            valor_total_calculado=reserva.valor_total_calculado
        )
        db.add(nova_reserva)
        db.commit()
        db.refresh(nova_reserva)
        return nova_reserva

    def listar_reservas(self, db: Session):
        return db.query(Reserva).all()