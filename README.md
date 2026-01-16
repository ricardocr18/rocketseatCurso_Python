# 🍽️ Daily Diet API - Sistema de Controle de Dieta

API REST completa para controle de dieta diária com autenticação de usuários e gerenciamento de refeições.

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
 Tabela `**user**`
```
 id          # Integer, PK
username    # String(80), único
password    # String(50)
```
Tabela `**meal**`
id          # Integer, PK
name        # String(100)
description # Text
date_time   # DateTime
is_on_diet  # Boolean
user_id     # Integer, FK → user.id


