from sqlalchemy.orm import Session
from src.repositories.usuario_repository import UsuarioRepository
from src.schemas.usuario import UsuarioCreate

class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def criar_usuario(self, db: Session, usuario: UsuarioCreate):
        return self.repository.criar_usuario(db, usuario)

    def listar_usuarios(self, db: Session):
        return self.repository.listar_usuarios(db)

    def deletar_usuario(self, db: Session, id_usuario: int):
        return self.repository.deletar_usuario(db, id_usuario)