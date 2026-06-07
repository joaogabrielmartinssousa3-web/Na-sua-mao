from fastapi import APIRouter, Depends, HTTPException
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

from fastapi import HTTPException, status
from pydantic import BaseModel

# 1. Esquema que define o que o front-end vai enviar no login
class UsuarioLogin(BaseModel):
    email: str
    senha: str

# 2. A Rota de Login Oficial
@router.post("/login")
def login(dados: UsuarioLogin, db: Session = Depends(get_db)):
    # Importação feita aqui dentro para evitar problemas de caminhos circulares no teu projeto
    from src.models.usuario import Usuario 
    
    # Procura o utilizador no banco de dados pelo e-mail
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()
    
    # Se não existir utilizador ou a senha estiver errada, bloqueia
    if not usuario or usuario.senha != dados.senha:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="E-mail ou senha incorretos"
        )
    
    # Se der tudo certo, devolve o token de acesso
    return {"access_token": f"token_do_usuario_{usuario.id_usuario}", "token_type": "bearer"}
@router.delete("/{id_usuario}")
def deletar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    sucesso = usuario_service.deletar_usuario(db, id_usuario)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"mensagem": "Usuário deletado com sucesso!"}
