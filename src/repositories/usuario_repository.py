from sqlalchemy.orm import Session
from src.models.usuario import Usuario
from src.schemas.usuario import UsuarioCreate

class UsuarioRepository:
    def criar_usuario(self, db: Session, usuario: UsuarioCreate):
        db_usuario = Usuario(**usuario.model_dump()) # ou usuario.dict()
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario

    def listar_usuarios(self, db: Session):
        return db.query(Usuario).all()

    def deletar_usuario(self, db: Session, id_usuario: int):
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if usuario:
            db.delete(usuario)
            db.commit()
            return True
        return False