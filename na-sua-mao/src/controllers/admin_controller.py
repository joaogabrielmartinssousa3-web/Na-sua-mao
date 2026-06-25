from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from src.middlewares.auth import require_admin, registrar_log
from src.services.avaliacao_service import resolver_denuncia
from models.models import Denuncia, StatusDenuncia, Usuario, Ferramenta, StatusFerramenta, Reserva

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def painel_admin(request: Request, db: Session = Depends(get_db), admin: Usuario = Depends(require_admin)):
    denuncias = db.query(Denuncia).filter(
        Denuncia.status_denuncia.in_([StatusDenuncia.PENDENTE, StatusDenuncia.EM_ANALISE])
    ).order_by(Denuncia.id_denuncia.desc()).all()

    total_usuarios = db.query(Usuario).count()
    total_ferramentas = db.query(Ferramenta).count()
    total_reservas = db.query(Reserva).count()

    return templates.TemplateResponse("admin/painel.html", {
        "request": request, "usuario": admin,
        "denuncias": denuncias,
        "total_usuarios": total_usuarios,
        "total_ferramentas": total_ferramentas,
        "total_reservas": total_reservas
    })

@router.get("/denuncias/{denuncia_id}", response_class=HTMLResponse)
async def detalhe_denuncia(request: Request, denuncia_id: int, db: Session = Depends(get_db), admin: Usuario = Depends(require_admin)):
    denuncia = db.query(Denuncia).filter(Denuncia.id_denuncia == denuncia_id).first()
    if not denuncia:
        return RedirectResponse("/admin/", status_code=302)
    return templates.TemplateResponse("admin/denuncia_detalhe.html", {
        "request": request, "usuario": admin, "denuncia": denuncia
    })

@router.post("/denuncias/{denuncia_id}/resolver")
async def resolver(request: Request, denuncia_id: int, resolucao: str = Form(...), db: Session = Depends(get_db), admin: Usuario = Depends(require_admin)):
    resolver_denuncia(db, denuncia_id, resolucao, admin.id_usuario)
    registrar_log(db, admin.id_usuario, "RESOLVER_DENUNCIA", f"Denúncia #{denuncia_id}")
    return RedirectResponse("/admin/", status_code=302)

@router.post("/usuarios/{usuario_id}/suspender")
async def suspender_usuario(request: Request, usuario_id: int, db: Session = Depends(get_db), admin: Usuario = Depends(require_admin)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if usuario:
        usuario.status_conta = "suspenso"
        db.commit()
        registrar_log(db, admin.id_usuario, "SUSPENDER_USUARIO", f"Usuário #{usuario_id}")
    return RedirectResponse("/admin/", status_code=302)

@router.post("/ferramentas/{ferramenta_id}/remover")
async def remover_ferramenta(request: Request, ferramenta_id: int, db: Session = Depends(get_db), admin: Usuario = Depends(require_admin)):
    ferramenta = db.query(Ferramenta).filter(Ferramenta.id_ferramenta == ferramenta_id).first()
    if ferramenta:
        ferramenta.status_ferramenta = StatusFerramenta.INATIVA
        db.commit()
        registrar_log(db, admin.id_usuario, "REMOVER_FERRAMENTA", f"Ferramenta #{ferramenta_id}")
    return RedirectResponse("/admin/", status_code=302)

@router.get("/usuarios", response_class=HTMLResponse)
async def listar_usuarios(
    request: Request, 
    page: int = 1, 
    limit: int = 50, 
    db: Session = Depends(get_db), 
    admin: Usuario = Depends(require_admin)
):
    
    offset = (page - 1) * limit
    
    
    total_usuarios = db.query(Usuario).count()
    
    
    usuarios = db.query(Usuario).offset(offset).limit(limit).all()
    
    return templates.TemplateResponse("admin/usuarios.html", {
        "request": request, 
        "usuario": admin, 
        "usuarios": usuarios,
        "page": page,
        "limit": limit,
        "total_usuarios": total_usuarios,
        "total_paginas": (total_usuarios + limit - 1) // limit
    })