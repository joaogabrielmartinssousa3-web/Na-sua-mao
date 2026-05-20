from fastapi import FastAPI

app = FastAPI(title="API Na Sua Mão")

@app.get("/")
def read_root():
    return {"mensagem": "API do sistema Na Sua Mão operando com sucesso!"}