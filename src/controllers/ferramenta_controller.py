from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.ferramenta import FerramentaCreate, FerramentaResponse
from src.services.ferramenta_service import FerramentaService

router = APIRouter(prefix="/ferramentas", tags=["Ferramentas"])
ferramenta_service = FerramentaService()

@router.post("/", response_model=FerramentaResponse)
def criar_ferramenta(ferramenta: FerramentaCreate, db: Session = Depends(get_db)):
    return ferramenta_service.criar_ferramenta(db, ferramenta)

@router.get("/", response_model=list[FerramentaResponse])
def listar_ferramentas(db: Session = Depends(get_db)):
    return ferramenta_service.listar_ferramentas(db)