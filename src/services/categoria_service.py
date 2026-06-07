from sqlalchemy.orm import Session
from src.repositories.categoria_repository import CategoriaRepository
from src.schemas.categoria import CategoriaCreate

class CategoriaService:
    def __init__(self):
        self.repository = CategoriaRepository()

    def criar_categoria(self, db: Session, categoria: CategoriaCreate):
        return self.repository.criar_categoria(db, categoria)

    def listar_categorias(self, db: Session):
        return self.repository.listar_categorias(db)

    def deletar_categoria(self, db: Session, id_categoria: int):
        return self.repository.deletar_categoria(db, id_categoria)