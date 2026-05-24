from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.usuario import UsuarioCreate
from src.services.usuario_service import UsuarioService


router = APIRouter(prefix="/usuarios", tags=["Usuários"])
usuario_service = UsuarioService()

@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    novo_usuario = usuario_service.criar_usuario(db, usuario)
    return {"mensagem": "Utilizador guardado com sucesso via Camadas!", "id_usuario": novo_usuario.id_usuario}