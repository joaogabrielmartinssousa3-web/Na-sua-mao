from fastapi import APIRouter, Depends, HTTPException
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
@router.delete("/{id_reserva}")
def deletar_reserva(id_reserva: int, db: Session = Depends(get_db)):
    sucesso = reserva_service.deletar_reserva(db, id_reserva)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    return {"mensagem": "Reserva deletada com sucesso!"}