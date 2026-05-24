from sqlalchemy.orm import Session
from src.repositories.reserva_repository import ReservaRepository
from src.schemas.reserva import ReservaCreate

class ReservaService:
    def __init__(self):
        self.repository = ReservaRepository()

    def criar_reserva(self, db: Session, reserva: ReservaCreate):
        
        return self.repository.criar_reserva(db, reserva)

    def listar_reservas(self, db: Session):
        return self.repository.listar_reservas(db)