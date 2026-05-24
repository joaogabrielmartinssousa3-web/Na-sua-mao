from sqlalchemy.orm import Session
from src.models.usuario import Usuario
from src.schemas.usuario import UsuarioCreate

class UsuarioRepository:
    def criar_usuario(self, db: Session, usuario_schema: UsuarioCreate):
        novo_usuario = Usuario(
            nome=usuario_schema.nome,
            email=usuario_schema.email,
            senha=usuario_schema.senha,
            cpf=usuario_schema.cpf,
            cep=usuario_schema.cep,
            telefone=usuario_schema.telefone
        )
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)
        return novo_usuario