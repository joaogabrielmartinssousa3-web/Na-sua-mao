from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.categoria import CategoriaCreate, CategoriaResponse
from src.services.categoria_service import CategoriaService

router = APIRouter(prefix="/categorias", tags=["Categorias"])
categoria_service = CategoriaService()

@router.post("/", response_model=CategoriaResponse)
def criar_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_service.criar_categoria(db, categoria)

@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return categoria_service.listar_categorias(db)

@router.delete("/{id_categoria}")
def deletar_categoria(id_categoria: int, db: Session = Depends(get_db)):
    sucesso = categoria_service.deletar_categoria(db, id_categoria)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return {"mensagem": "Categoria deletada com sucesso!"}