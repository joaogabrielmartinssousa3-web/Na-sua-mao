from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.usuario import UsuarioCreate
from src.schemas.ferramenta import FerramentaCreate 
from src.database import engine, get_db
from src.models.usuario import Base, Usuario
from src.models.ferramenta import Ferramenta 


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Na Sua Mão - API")

@app.get("/")
def read_root():
    return {"message": "API Na Sua Mão está rodando perfeitamente!"}


@app.post("/usuarios", tags=["Usuários"])
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
   
    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha,
        cpf=usuario.cpf,
        cep=usuario.cep,
        telefone=usuario.telefone
    )
    
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    return {"mensagem": "Usuário salvo com sucesso no MySQL!", "usuario_id": novo_usuario.id_usuario}
@app.post("/ferramentas", tags=["Ferramentas"])
def criar_ferramenta(ferramenta: FerramentaCreate, db: Session = Depends(get_db)):
    nova_ferramenta = Ferramenta(
        nome=ferramenta.nome,
        descricao=ferramenta.descricao,
        disponivel=ferramenta.disponivel
    )
    
    db.add(nova_ferramenta)
    db.commit()
    db.refresh(nova_ferramenta)
    
    return {"mensagem": "Ferramenta salva com sucesso!", "ferramenta": nova_ferramenta}