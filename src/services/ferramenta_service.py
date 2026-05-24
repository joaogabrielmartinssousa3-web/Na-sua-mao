from sqlalchemy.orm import Session
from src.repositories.ferramenta_repository import FerramentaRepository
from src.schemas.ferramenta import FerramentaCreate

class FerramentaService:
    def __init__(self):
        self.repository = FerramentaRepository()

    def criar_ferramenta(self, db: Session, ferramenta: FerramentaCreate):
        return self.repository.criar_ferramenta(db, ferramenta)

    def listar_ferramentas(self, db: Session):
        return self.repository.listar_ferramentas(db)