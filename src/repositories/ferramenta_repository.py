from sqlalchemy.orm import Session
from src.models.ferramenta import Ferramenta
from src.schemas.ferramenta import FerramentaCreate

class FerramentaRepository:
    def criar_ferramenta(self, db: Session, ferramenta: FerramentaCreate):
        db_ferramenta = Ferramenta(**ferramenta.model_dump()) # ou ferramenta.dict()
        db.add(db_ferramenta)
        db.commit()
        db.refresh(db_ferramenta)
        return db_ferramenta

    def listar_ferramentas(self, db: Session):
        return db.query(Ferramenta).all()

    def deletar_ferramenta(self, db: Session, id_ferramenta: int):
        ferramenta = db.query(Ferramenta).filter(Ferramenta.id_ferramenta == id_ferramenta).first()
        if ferramenta:
            db.delete(ferramenta)
            db.commit()
            return True
        return False