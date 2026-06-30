from sqlalchemy.orm import Session
from sqlalchemy import func
from models.models import Avaliacao


def salvar_avaliacao(db: Session, reserva_id: int, avaliador_id: int, avaliado_id: int, nota: int, comentario: str) -> Avaliacao:
    avaliacao = Avaliacao(
        id_reserva=reserva_id,
        id_avaliador=avaliador_id,
        id_avaliado=avaliado_id,
        nota=nota,
        comentario=comentario
    )
    db.add(avaliacao)
    db.commit()
    db.refresh(avaliacao)
    return avaliacao


def buscar_avaliacoes_por_usuario(db: Session, avaliado_id: int) -> list[Avaliacao]:
    return db.query(Avaliacao).filter(Avaliacao.id_avaliado == avaliado_id).all()


def calcular_media_reputacao(db: Session, avaliado_id: int) -> float:
    resultado = db.query(func.avg(Avaliacao.nota)).filter(
        Avaliacao.id_avaliado == avaliado_id
    ).scalar()
    return round(float(resultado), 1) if resultado else 0.0


def avaliacao_ja_existe(db: Session, reserva_id: int, avaliador_id: int) -> bool:
    return db.query(Avaliacao).filter(
        Avaliacao.id_reserva == reserva_id,
        Avaliacao.id_avaliador == avaliador_id
    ).first() is not None