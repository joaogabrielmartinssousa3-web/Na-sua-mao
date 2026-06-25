# 🔧 Na Sua Mão — Plataforma de Aluguel de Ferramentas
  
Universidade Católica de Brasília (UCB) - 2026

**Equipe de Desenvolvimento:**
* João Victor Martins Sousa
* João Gabriel Martins Sousa
* Enzo Reis Alves
* Gabriel Dias Dos Santos
* Arthur Leastro Gonçalves De Siqueira

**Stack Tecnológica:** Python 3 | FastAPI | Jinja2 | TailwindCSS | SQLite / MySQL 8.0

---

## 🚀 Como Executar

### 1. Instalar dependências

```bash
cd na-sua-mao
pip install -r requirements.txt
```

### 2. Executar a aplicação

```bash
python main.py
```

Acesse: **http://localhost:8000**

---
Conta Admin -
Usuário: Admin@nasua.mao

Senha: admin123

---

## 🗺️ Rotas Principais

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Home — busca de ferramentas |
| GET/POST | `/login` | Autenticação |
| GET/POST | `/cadastro` | Cadastro de usuário |
| GET/POST | `/perfil` | Editar perfil |
| GET | `/ferramentas/{id}` | Detalhe da ferramenta |
| GET/POST | `/ferramentas/nova` | Cadastrar ferramenta |
| GET | `/minhas-ferramentas` | Ferramentas do usuário |
| GET | `/meus-alugueis` | Reservas do usuário |
| GET | `/reservas/{id}` | Detalhe da reserva |
| POST | `/reservas/solicitar` | Solicitar aluguel |
| POST | `/reservas/{id}/confirmar` | Confirmar (locador) |
| POST | `/reservas/{id}/entregar` | Registrar entrega |
| POST | `/reservas/{id}/devolver` | Registrar devolução |
| POST | `/reservas/{id}/cancelar` | Cancelar reserva |
| POST | `/reservas/{id}/avaliar` | Avaliar experiência |
| POST | `/reservas/{id}/denuncia` | Abrir denúncia |
| GET | `/admin/` | Painel admin |
| GET | `/admin/usuarios` | Lista de usuários |
| GET | `/admin/denuncias/{id}` | Analisar denúncia |

---

## 📋 Casos de Uso Implementados

| UC | Descrição | Status |
|----|-----------|--------|
| UC-001 | Cadastrar Ferramenta | ✅ |
| UC-002 | Solicitar Aluguel | ✅ |
| UC-003 | Avaliar Experiência | ✅ |
| UC-004 | Gerenciar Perfil | ✅ |
| UC-005 | Registrar Devolução | ✅ |
| UC-006 | Enviar Mensagens | ✅ |
| UC-007 | Cancelar Reserva | ✅ |
| UC-008 | Consultar Reputação | ✅ |
| UC-009 | Acompanhar Status | ✅ |
| UC-010 | Efetuar Login | ✅ |
| UC-011 | Moderação Admin | ✅ |
| UC-012 | Abrir Denúncia | ✅ |
| UC-013 | Resolver Denúncia | ✅ |

---


## 🗄️ Banco de Dados

Por padrão usa **SQLite** (arquivo `na_sua_mao.db` criado automaticamente).

Para usar **MySQL 8.0** :
```bash
export DATABASE_URL="mysql+pymysql://user:password@localhost/na_sua_mao"
pip install pymysql
```
