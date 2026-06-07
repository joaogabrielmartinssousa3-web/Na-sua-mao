from sqlalchemy.orm import Session
from src.models.categoria import Categoria
from src.schemas.categoria import CategoriaCreate

class CategoriaRepository:
    def criar_categoria(self, db: Session, categoria: CategoriaCreate):
        db_categoria = Categoria(**categoria.model_dump()) # ou categoria.dict()
        db.add(db_categoria)
        db.commit()
        db.refresh(db_categoria)
        return db_categoria

    def listar_categorias(self, db: Session):
        return db.query(Categoria).all()

    def deletar_categoria(self, db: Session, id_categoria: int):
        categoria = db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
        if categoria:
            db.delete(categoria)
            db.commit()
            return True
        return False