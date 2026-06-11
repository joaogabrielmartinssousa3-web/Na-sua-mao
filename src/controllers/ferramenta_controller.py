from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.ferramenta import FerramentaCreate, FerramentaResponse
from src.services.ferramenta_service import FerramentaService
import shutil


router = APIRouter(prefix="/ferramentas", tags=["Ferramentas"])
ferramenta_service = FerramentaService()


@router.post("/upload-foto/")
async def upload_foto(file: UploadFile = File(...)):
    
    file_path = f"images/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    
    return {"url": f"http://127.0.0.1:8000/{file_path}"}

@router.post("/", response_model=FerramentaResponse)
def criar_ferramenta(ferramenta: FerramentaCreate, db: Session = Depends(get_db)):
    return ferramenta_service.criar_ferramenta(db, ferramenta)

@router.get("/", response_model=list[FerramentaResponse])
def listar_ferramentas(db: Session = Depends(get_db)):
    return ferramenta_service.listar_ferramentas(db)

@router.get("/{id_ferramenta}")
def buscar_ferramenta(id_ferramenta: int, db: Session = Depends(get_db)):
    return ferramenta_service.obter_ferramenta_por_id(db, id_ferramenta)
@router.delete("/{id_ferramenta}")
def deletar_ferramenta(id_ferramenta: int, db: Session = Depends(get_db)):
    sucesso = ferramenta_service.deletar_ferramenta(db, id_ferramenta)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Ferramenta não encontrada")
    return {"mensagem": "Ferramenta deletada com sucesso!"}
