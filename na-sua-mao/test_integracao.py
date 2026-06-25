import os
import pytest
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from models.models import Usuario
from src.integrations.cpf_service import validar_cpf_externo, formatar_cpf
from src.integrations.storage_service import salvar_imagem

# Configuração do Banco de Dados em Memória para o Teste
@pytest.fixture(scope="function")
def db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)
    engine.dispose() 

def test_integracao_banco_de_dados(db):
    """
    Objetivo: Garantir que o SQLAlchemy consegue inserir, ler e atualizar um registro real no banco.
    """
    # 1. CREATE (Inserir)
    novo_usuario = Usuario(
        nome="Teste Integração",
        email="teste@integracao.com",
        senha="hash",
        cpf="000.000.000-00",
        data_nascimento=date(1990, 1, 1),
        status_conta="ativo"
    )
    db.add(novo_usuario)
    db.commit()

    # 2. READ (Ler)
    usuario_salvo = db.query(Usuario).filter(Usuario.email == "teste@integracao.com").first()
    assert usuario_salvo is not None
    assert usuario_salvo.nome == "Teste Integração"

    # 3. UPDATE (Atualizar)
    usuario_salvo.status_conta = "suspenso"
    db.commit()
    
    usuario_atualizado = db.query(Usuario).filter(Usuario.email == "teste@integracao.com").first()
    assert usuario_atualizado.status_conta == "suspenso"

def test_integracao_servico_cpf():
    """
    Objetivo: Validar o componente de CPF rejeitando formatos inválidos e formatando corretamente.
    """
    # Testa a formatação
    cpf_formatado = formatar_cpf("12345678901")
    assert cpf_formatado == "123.456.789-01"

    # Testa a validação matemática (111.111.111-11 é barrado pela sua regra de dígitos iguais)
    cpf_valido = validar_cpf_externo("111.111.111-11")
    assert cpf_valido is False

def test_integracao_servico_storage():
    """
    Objetivo: Garantir que o PIL consegue processar os bytes de uma imagem e salvá-la no disco.
    """
    
    bytes_imagem = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
    
    
    caminho_salvo = salvar_imagem(bytes_imagem, "teste.png")
    
    
    caminho_normalizado = caminho_salvo.replace("\\", "/")
    
    
    assert caminho_normalizado.startswith("/static/uploads/")
    assert caminho_normalizado.endswith(".jpg") 
    
    
    caminho_fisico = caminho_salvo.lstrip("/")
    if os.path.exists(caminho_fisico):
        os.remove(caminho_fisico)