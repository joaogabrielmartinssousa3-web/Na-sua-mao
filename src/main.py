from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <-- NOVA IMPORTAÇÃO
from src.controllers import usuario_controller, categoria_controller, ferramenta_controller, reserva_controller

app = FastAPI(title="API Na Sua Mão")

# --- CONFIGURAÇÃO DE CORS (A MÁGICA DA CONEXÃO) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, colocamos o link real do site aqui. Em testes, o "*" libera para o seu localhost.
    allow_credentials=True,
    allow_methods=["*"], # Permite POST, GET, PUT, DELETE
    allow_headers=["*"], # Permite envio de JSON e tokens
)
# --------------------------------------------------

app.include_router(usuario_controller.router)
app.include_router(categoria_controller.router)
app.include_router(ferramenta_controller.router)
app.include_router(reserva_controller.router)