# 🍽️ Daily Diet API - Sistema de Controle de Dieta

API REST completa para controle de dieta diária com autenticação de usuários e gerenciamento de refeições.<br><br>

## 📋 Sobre o Projeto
Uma API desenvolvida em Flask que permite aos usuários registrar e acompanhar suas refeições diárias. O sistema oferece autenticação baseada em sessões, CRUD completo de usuários e refeições, além de métricas sobre a dieta.

## ✨ Funcionalidades
### 🔐 Autenticação
Login/Logout com sessões persistentes
Proteção de rotas privadas
Validação de credenciais

### 👥 Gerenciamento de Usuários
Cadastro de múltiplos usuários
Atualização de perfil
Exclusão de conta (com proteção contra auto-exclusão)
Isolamento de dados por usuário

### 🍴 Controle de Refeições
Registro de refeições com nome, descrição, data/hora
Marcação de refeições dentro/fora da dieta
Edição completa de refeições
Exclusão de refeições
Listagem ordenada por data
Métricas detalhadas da dieta

### 🚀 Tecnologias
Flask - Framework web minimalista
Flask-SQLAlchemy - ORM para banco de dados
Flask-Login - Gerenciamento de sessões
SQLite - Banco de dados relacional


## 📁 Estrutura do Projeto
```
sample-flask-auth/
├── app.py                 # Rotas e lógica principal
├── database.py            # Configuração do SQLAlchemy
├── models/
│   ├── user.py           # Model de Usuário
│   └── meal.py           # Model de Refeição
├── instance/
│   └── database.db       # Banco SQLite (criado automaticamente)
└── requirements.txt      # Dependências do projeto
```


## 🗃️ Modelo de Dados
### Tabela `` `user` ``
```
 id          # Integer, PK
username    # String(80), único
password    # String(50)
```
### Tabela `` `meal` ``
```
id          # Integer, PK
name        # String(100)
description # Text
date_time   # DateTime
is_on_diet  # Boolean
user_id     # Integer, FK → user.id
```

Relacionamento: 1 usuário → N refeições

## 🛣️ Rotas da API
### 🔑 Autenticação
Login

```
POST /login
Content-Type: application/json

{
    "username": "maria",
    "password": "123"
}
```

Resposta (200):
```
{
    "message": "Credenciais estão ok, você está Logado no Sistema!!!"
}
```

Logout
```
GET /logout
```
Resposta (200):
```
{
    "message": "Logout realizado com sucesso"
}
```
## 👤 Usuários
Criar Usuário
```
POST /user
Content-Type: application/json

{
    "username": "joao",
    "password": "456"
}
```

Resposta (201):

```
{
    "message": "Usuário criado com sucesso",
    "user": {
        "id": 2,
        "username": "joao"
    }
}
```
Buscar Usuário
```
GET /user/1
Authorization: Required (login)
```
Resposta (200):
```
{
    "id": 1,
    "username": "maria",
    "total_meals": 5
}
```
Atualizar Usuário
```
PUT /user/1
Authorization: Required (login)
Content-Type: application/json

{
    "username": "maria_silva",
    "password": "nova_senha"
}
```
Resposta (200):
```
{
    "message": "Usuário atualizado com sucesso"
}
```
Deletar Usuário
```
DELETE /user/2
Authorization: Required (login)
```
Resposta (200):
```
{
    "message": "Usuário deletado com sucesso"
}
```
⚠️ Nota: Não é possível deletar o próprio usuário enquanto logado.

## 🍽️ Refeições

Criar Refeição
```
POST /meal
Authorization: Required (login)
Content-Type: application/json

{
    "name": "Café da manhã",
    "description": "Ovos mexidos com torrada integral",
    "date_time": "2026-01-16T08:00:00",
    "is_on_diet": true
}
```
Resposta (201):
```
{
    "message": "Refeição criada com sucesso",
    "meal": {
        "id": 1,
        "name": "Café da manhã",
        "description": "Ovos mexidos com torrada integral",
        "date_time": "2026-01-16T08:00:00",
        "is_on_diet": true,
        "user_id": 1
    }
}
```

Listar Todas as Refeições
```
GET /meals
Authorization: Required (login)
```
Resposta (200):
```
{
    "meals": [
        {
            "id": 1,
            "name": "Café da manhã",
            "description": "Ovos mexidos",
            "date_time": "2026-01-16T08:00:00",
            "is_on_diet": true,
            "user_id": 1
        }
    ],
    "total": 1
}
```

Buscar Refeição Específica
```
GET /meal/1
Authorization: Required (login)
```
Resposta (200):
```
{
    "id": 1,
    "name": "Café da manhã",
    "description": "Ovos mexidos",
    "date_time": "2026-01-16T08:00:00",
    "is_on_diet": true,
    "user_id": 1
}
```

Atualizar Refeição
```
PUT /meal/1
Authorization: Required (login)
Content-Type: application/json

{
    "name": "Café da manhã MODIFICADO",
    "description": "Tapioca com queijo",
    "date_time": "2026-01-16T08:30:00",
    "is_on_diet": false
}
```
Resposta (200):
```
{
    "message": "Refeição atualizada com sucesso",
    "meal": {
        "id": 1,
        "name": "Café da manhã MODIFICADO",
        "description": "Tapioca com queijo",
        "date_time": "2026-01-16T08:30:00",
        "is_on_diet": false,
        "user_id": 1
    }
}
```

Deletar Refeição
```
DELETE /meal/1
Authorization: Required (login)
```

Resposta (200):
```
{
    "message": "Refeição deletada com sucesso"
}
```

Buscar Usuário com Suas Refeições
```
GET /user/1/meals
Authorization: Required (login)
```
Resposta (200):
```
{
    "user": {
        "id": 1,
        "username": "maria"
    },
    "meals": [
        {
            "id": 1,
            "name": "Café da manhã",
            "description": "...",
            "date_time": "2026-01-16T08:00:00",
            "is_on_diet": true,
            "user_id": 1
        }
    ],
    "total_meals": 1
}
```

## 🚀 Como Executar

### 1️⃣ **Clonar o repositório**

```bash
git clone -b nivel2Desafio https://github.com/ricardocr18/rocketseatCurso_Python.git nivel2Desafio
cd nivel2Desafio
```

### 2️⃣ **Criar ambiente virtual**

```bash
python -m venv .venv
```

**Ativar no Windows:**
```bash
.venv\Scripts\activate
```

**Ativar no Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3️⃣ **Instalar dependências**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Executar a aplicação**

```bash
python app.py
```

Servidor rodando em: http://127.0.0.1:5000

## 📦 Dependências
```
Flask==2.3.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.2
Werkzeug==2.3.0
```

## 🧪 Testando com Postman
### Fluxo Completo
Criar usuário: POST http://127.0.0.1:5000/user
Fazer login: POST http://127.0.0.1:5000/login
Criar refeição: POST http://127.0.0.1:5000/meal
Ver todas as refeições: GET http://127.0.0.1:5000/meals
Logout: GET http://127.0.0.1:5000/logout

Observação: É necessario estar logado para executar as ações

## 👨‍💻 Autor
Ricardo C. Ribeiro


