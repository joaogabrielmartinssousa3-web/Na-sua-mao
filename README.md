# 🛠️ Na Sua Mão - API (Backend)

Bem-vindo ao repositório do backend do sistema **Na Sua Mão**

## 🚀 Como rodar o projeto localmente

Siga estes passos exatos para configurar o ambiente e rodar o servidor no seu computador:

1.  **Clone o repositório:**
    Abra o seu terminal e use o comando abaixo:
    ```bash
    git clone https://github.com/Na-sua-mao/na-sua-mao-api.git

    ```

2.  **Configurar o Ambiente Virtual:**
    Entre na pasta do projeto e use os comandos abaixo no terminal:

    * **Para Criar o ambiente:**
        ```bash
        python -m venv venv
        ```
    * **Para Ativar o ambiente (No Windows):**
        ```powershell
        .\venv\Scripts\activate
        ```
    * *(Caso use Mac ou Linux, o comando de ativação é: `source venv/bin/activate`)*

3.  **Instalar as dependências:**
    Com o ambiente virtual ativado, rode:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Iniciar o servidor local:**
    Use o comando abaixo para colocar a API no ar:
    ```bash
    uvicorn src.main:app --reload
    ```

5.  **Acesse no navegador:**
    * Ver a API rodando: Abra `http://localhost:8000`
    * **Documentação automática (FastAPI):** Acesse `http://localhost:8000/docs` para testar os endpoints.
    


