from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.usuario import UsuarioCreate
from src.database import engine, get_db
from src.models.usuario import Base, Usuario

# Esta linha diz ao SQLAlchemy para ler os nossos modelos e criar as tabelas no SQLite se não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Na Sua Mão - API")

@app.get("/")
def read_root():
    return {"message": "API Na Sua Mão está rodando perfeitamente!"}

# Atualizámos a rota para receber o 'db' como dependência
@app.post("/usuarios", tags=["Usuários"])
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # 1. Transformar o Schema do FastAPI num Modelo do Banco de Dados
    novo_usuario = Usuario(
        nome=usuario.nome,
        cpf=usuario.cpf,
        endereco=usuario.endereco
    )
    
    # 2. Salvar no Banco de Dados
    db.add(novo_usuario) # Adiciona na fila
    db.commit()          # Salva de forma definitiva
    db.refresh(novo_usuario) # Atualiza o objeto para pegar o ID gerado automaticamente
    
    return {
        "mensagem": "Usuário cadastrado com sucesso de verdade!",
        "usuario": {
            "id": novo_usuario.id,
            "nome": novo_usuario.nome,
            "cpf": novo_usuario.cpf,
            "endereco": novo_usuario.endereco
        }
    }