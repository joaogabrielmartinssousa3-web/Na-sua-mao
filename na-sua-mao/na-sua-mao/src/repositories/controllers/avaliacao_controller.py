from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from src.middlewares.auth import require_login
from src.services.avaliacao_service import avaliar_experiencia
from src.repositories.avaliacao_repository import buscar_avaliacoes_por_usuario, calcular_media_reputacao
from models.models import Usuario

router = APIRouter(tags=["Avaliações"])
templates = Jinja2Templates(directory="templates")


@router.get("/usuarios/{usuario_id}/reputacao", response_class=HTMLResponse)
async def ver_reputacao(
    request: Request,
    usuario_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(require_login)
):
    avaliado = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if not avaliado:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

    avaliacoes = buscar_avaliacoes_por_usuario(db, usuario_id)
    media = calcular_media_reputacao(db, usuario_id)

    return templates.TemplateResponse("perfil_reputacao.html", {
        "request": request,
        "usuario": usuario,
        "avaliado": avaliado,
        "avaliacoes": avaliacoes,
        "media": media,
        "total_alugueis": avaliado.total_alugueis
    })