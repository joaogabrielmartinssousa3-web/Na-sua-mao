from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.reserva import ReservaCreate, ReservaResponse
from src.services.reserva_service import ReservaService

router = APIRouter(prefix="/reservas", tags=["Reservas"])
reserva_service = ReservaService()

@router.post("/", response_model=ReservaResponse)
def criar_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    return reserva_service.criar_reserva(db, reserva)

@router.get("/", response_model=list[ReservaResponse])
def listar_reservas(db: Session = Depends(get_db)):
    return reserva_service.listar_reservas(db)