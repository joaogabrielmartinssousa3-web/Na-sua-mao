from sqlalchemy.orm import Session
from src.models.categoria import Categoria
from src.schemas.categoria import CategoriaCreate

class CategoriaRepository:
    def criar_categoria(self, db: Session, categoria: CategoriaCreate):
        nova_categoria = Categoria(nome_categoria=categoria.nome_categoria)
        db.add(nova_categoria)
        db.commit()
        db.refresh(nova_categoria)
        return nova_categoria

    def listar_categorias(self, db: Session):
        return db.query(Categoria).all()