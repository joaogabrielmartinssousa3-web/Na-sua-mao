import pytest
from unittest.mock import MagicMock
from src.services.avaliacao_service import validar_comentario, avaliar_experiencia
from models.models import Reserva, StatusReserva, Avaliacao


# ───────────────────────────────────────────
# TESTES UNITÁRIOS
# ───────────────────────────────────────────

class TestValidarComentario:

    def test_comentario_valido(self):
        assert validar_comentario("Ótimo vizinho, muito atencioso!") == True

    def test_comentario_vazio(self):
        assert validar_comentario("") == False

    def test_comentario_curto(self):
        assert validar_comentario("ok") == False

    def test_comentario_com_palavrao(self):
        assert validar_comentario("Foi muito merda esse aluguel") == False

    def test_comentario_com_palavrao_maiusculo(self):
        assert validar_comentario("Foi MERDA esse aluguel") == False


class TestCalculoMedia:

    def test_media_simples(self):
        notas = [5, 4, 3]
        media = round(sum(notas) / len(notas), 1)
        assert media == 4.0

    def test_media_nota_maxima(self):
        notas = [5, 5, 5]
        media = round(sum(notas) / len(notas), 1)
        assert media == 5.0

    def test_media_nota_minima(self):
        notas = [1, 1, 1]
        media = round(sum(notas) / len(notas), 1)
        assert media == 1.0

    def test_media_sem_avaliacoes(self):
        notas = []
        media = round(sum(notas) / len(notas), 1) if notas else 0.0
        assert media == 0.0


# ───────────────────────────────────────────
# TESTE DE INTEGRAÇÃO
# ───────────────────────────────────────────

class TestAvaliarExperiencia:

    def test_reserva_nao_encontrada(self):
        db = MagicMock()
        db.query().filter().first.return_value = None
        resultado = avaliar_experiencia(db, reserva_id=99, avaliador_id=1, nota=5, comentario="Ótimo!")
        assert "erro" in resultado

    def test_reserva_nao_finalizada(self):
        db = MagicMock()
        reserva = MagicMock()
        reserva.status_reserva = StatusReserva.EM_USO
        db.query().filter().first.return_value = reserva
        resultado = avaliar_experiencia(db, reserva_id=1, avaliador_id=1, nota=5, comentario="Ótimo!")
        assert "erro" in resultado

    def test_comentario_invalido(self):
        db = MagicMock()
        reserva = MagicMock()
        reserva.status_reserva = StatusReserva.FINALIZADO
        db.query().filter().first.return_value = reserva
        resultado = avaliar_experiencia(db, reserva_id=1, avaliador_id=1, nota=5, comentario="merda")
        assert "erro" in resultado