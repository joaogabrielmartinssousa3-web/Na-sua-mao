from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define onde o arquivo do banco de dados SQLite vai ser guardado localmente
SQLALCHEMY_DATABASE_URL = "sqlite:///./nasuamao.db"

# O engine é o motor que vai gerir a comunicação com o ficheiro do banco
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria as sessões de conversação com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função auxiliar (Dependency) para abrir e fechar a conexão automaticamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()