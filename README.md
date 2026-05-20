# 🛠️ Na Sua Mão - API (Backend)

Bem-vindo ao repositório do backend do sistema **Na Sua Mão**

## 🚀 Como rodar o projeto localmente

Para que todos da equipe consigam rodar o servidor no próprio computador, sigam estes passos:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SeuUsuario/na-sua-mao-api.git](https://github.com/SeuUsuario/na-sua-mao-api.git)

2.Crie o ambiente virtual

python -m venv venv
.\venv\Scripts\activate  # No Windows

3.Instale as dependências

pip install -r requirements.txt

4.Inicie o servidor local

uvicorn src.main:app --reload

5.Acesse no navegador

Abra http://localhost:8000 para ver a API rodando. A documentação automática do FastAPI estará disponível em http://localhost:8000/docs.

