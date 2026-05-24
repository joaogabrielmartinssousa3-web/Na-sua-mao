from fastapi import FastAPI
from src.controllers import usuario_controller, categoria_controller, ferramenta_controller, reserva_controller

app = FastAPI(title="API Na Sua Mão")

app.include_router(usuario_controller.router)
app.include_router(categoria_controller.router)
app.include_router(ferramenta_controller.router)
app.include_router(reserva_controller.router) 