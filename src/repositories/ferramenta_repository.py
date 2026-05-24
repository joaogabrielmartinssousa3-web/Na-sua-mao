from sqlalchemy.orm import Session
from src.models.ferramenta import Ferramenta
from src.schemas.ferramenta import FerramentaCreate

class FerramentaRepository:
    def criar_ferramenta(self, db: Session, ferramenta: FerramentaCreate):
        nova_ferramenta = Ferramenta(
            id_locador=ferramenta.id_locador,
            id_categoria=ferramenta.id_categoria,
            titulo=ferramenta.titulo,
            descricao=ferramenta.descricao,
            voltagem=ferramenta.voltagem,
            estado_conservacao=ferramenta.estado_conservacao,
            preco_diaria=ferramenta.preco_diaria
        )
        db.add(nova_ferramenta)
        db.commit()
        db.refresh(nova_ferramenta)
        return nova_ferramenta

    def listar_ferramentas(self, db: Session):
        return db.query(Ferramenta).all()