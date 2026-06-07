from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.repositories.reserva_repository import ReservaRepository
from src.schemas.reserva import ReservaCreate
from src.models.ferramenta import Ferramenta 

class ReservaService:
    def __init__(self):
        self.repository = ReservaRepository()

    def criar_reserva(self, db: Session, reserva: ReservaCreate):
        # 1. Procurar a ferramenta para saber quanto custa a diária
        ferramenta = db.query(Ferramenta).filter(Ferramenta.id_ferramenta == reserva.id_ferramenta).first()
        
        if not ferramenta:
            raise HTTPException(status_code=404, detail="Ferramenta não encontrada no banco de dados.")

        # 2. Calcular a diferença de dias com os nomes exatos do seu modelo
        diferenca_dias = (reserva.data_prevista_fim - reserva.data_prevista_inicio).days
        
        # Regra de negócio: Se a pessoa alugar e devolver no mesmo dia, cobra-se 1 diária no mínimo
        if diferenca_dias <= 0:
            diferenca_dias = 1

        # 3. O motor matemático
        reserva.valor_total_calculado = diferenca_dias * ferramenta.preco_diaria

        # 4. Envia para o banco de dados
        return self.repository.criar_reserva(db, reserva)

    def listar_reservas(self, db: Session):
        return self.repository.listar_reservas(db)

    def deletar_reserva(self, db: Session, id_reserva: int):
        return self.repository.deletar_reserva(db, id_reserva)