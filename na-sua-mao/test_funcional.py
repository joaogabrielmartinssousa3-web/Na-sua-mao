from fastapi.testclient import TestClient
from main import app 

# Cria o "navegador fantasma" para testar as rotas
client = TestClient(app)

def test_carregar_pagina_inicial():
    """
    Objetivo: Verificar se a Home Page (catálogo) carrega corretamente para um visitante.
    """
    response = client.get("/")
    
    # Verifica se a página carregou com sucesso (Status 200)
    assert response.status_code == 200
    # Verifica se o título correto está na tela (baseado no index.html)
    assert "Ferramentas na sua Vizinhança" in response.text

def test_bloqueio_de_rota_protegida():
    """
    Objetivo: Garantir que um usuário não logado seja expulso ao tentar acessar o perfil.
    """
    # Tenta acessar uma rota que exige o Depends(require_login)
    # Como o TestClient não evita redirecionamentos por padrão, precisamos capturar
    response = client.get("/perfil", follow_redirects=False)
    
    # Verifica se o sistema barrou e mandou fazer login (Status 303 Redirect)
    assert response.status_code == 303
    assert response.headers["location"] == "/login"

def test_tentativa_de_login_invalido():
    """
    Objetivo: Simular o preenchimento do formulário de login com dados errados.
    """
    # Envia os dados como se fosse o formulário HTML do login.html
    dados_formulario = {
        "email": "hacker@vizinhança.com",
        "senha": "senhaincorreta"
    }
    response = client.post("/login", data=dados_formulario)
    
    # A página recarrega (Status 200), mas deve exibir a mensagem de erro da controller
    assert response.status_code == 200
    assert "E-mail ou senha incorretos" in response.text