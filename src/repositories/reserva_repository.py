from sqlalchemy.orm import Session
from src.models.reserva import Reserva
from src.schemas.reserva import ReservaCreate

class ReservaRepository:
    def criar_reserva(self, db: Session, reserva: ReservaCreate):
        db_reserva = Reserva(**reserva.model_dump()) # ou reserva.dict() dependendo da versão do Pydantic
        db.add(db_reserva)
        db.commit()
        db.refresh(db_reserva)
        return db_reserva

    def listar_reservas(self, db: Session):
        return db.query(Reserva).all()

    def deletar_reserva(self, db: Session, id_reserva: int):
        reserva = db.query(Reserva).filter(Reserva.id_reserva == id_reserva).first()
        if reserva:
            db.delete(reserva)
            db.commit()
            return True
        return False