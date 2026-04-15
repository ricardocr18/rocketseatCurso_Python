# 🚀 Nível 3 - Comunicação em tempo real com Flask

Bem-vindo ao diretório do **Nível 3**. Este espaço centraliza o aprendizado prático de APIs robustas com Flask e Flask-SocketIO

## 📂 Estrutura do Diretório

1.  **📝 [atividadeProposta](#-atividadeproposta)**: Simulador PIX, plicação back-end em Flask com comunicação em tempo real via SocketIO.
2.  **🎮 [desafioPrático](#-desafiopratico)**: Foi o Desafio do Nivel 3, desenvolvimento de uma aplicação de **Chat Multiusuário**.

---

# 📝 atividadeProposta
Esta pasta contém um projeto exemplo em **Flask + Flask-SocketIO** que simula um ecossistema de pagamentos via PIX.

### 🛠️ Funcionalidades Principais
* **Geração de Pagamentos:** Criação de transações PIX com QR Codes fictícios.
* **Webhooks de Confirmação:** Simulação de retorno bancário para confirmação de pagamento.
* **Real-time:** Notificações instantâneas via SocketIO.
* **Interface:** Visualização de status de pagamento em páginas HTML dinâmicas.

### 🏗️ Estrutura do Projeto
A organização dos arquivos segue o padrão de responsabilidades do Flask:
* **`app.py`**: Inicialização do Flask + SocketIO e definição das rotas principais.
* **`db_models/`**: Definição dos modelos de dados (ex.: `payment.py`).
* **`repository/`**: Camada de conexão e persistência com o banco de dados (`database.py`).
* **`static/`**: Arquivos estáticos como CSS e imagens dos QR Codes gerados.
* **`templates/`**: Páginas HTML renderizadas pelo servidor.
* **`instance/`**: Armazena o banco de dados local (SQLite). *Nota: Esta pasta costuma ser excluída do versionamento.*

### 🔌 Endpoints Importantes

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `POST` | `/payments/pix` | Cria um pagamento (Body JSON: `{ "value": 150.0 }`) |
| `GET` | `/payments/pix/qr_code/<file>` | Recupera a imagem do QR Code gerado |
| `POST` | `/payments/pix/confirmation` | Webhook para confirmar pagamento |
| `GET` | `/payments/pix/<id>` | Renderiza a página de status do pagamento |

### 🚀 Como Rodar a Aplicação

1.  **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Criar o Banco de Dados:**
    ```bash
    python -c "from app import app; from repository.database import db; with app.app_context(): db.create_all(); print('Tabelas criadas!')"
    ```
3.  **Iniciar o servidor:**
    ```bash
    python app.py
    ```
    *Acesse em: `http://127.0.0.1:5000`*

### 📸 Demonstração do Browser
*Pesquisa de dados via ID (Exemplo ID 5) e Confirmação de Pagamento (Exemplo ID 1):*
<img width="600" alt="Tela de Cadastro" src="https://github.com/user-attachments/assets/91cac3c7-88bb-491e-89a3-71ce6c5cafcf" />
<img width="600" alt="Pagamento Realizado" src="https://github.com/user-attachments/assets/15b3c33f-db46-48ec-ab45-ccba43d57633" />

### 📥 Acesso (Download Facilitado)
Para facilitar a visualização ou baixar apenas o conteúdo desta pasta:

1.  🚀 **Visualização Rápida:** [Clique aqui para abrir o código no Editor Web](https://github.dev/ricardocr18/rocketseatCurso_Python/tree/main/nivel3/atividadeProposta) (Pressione `.` no teclado).
2.  📦 **Download Direto (.zip):** [Clique aqui para baixar apenas esta pasta](https://download-directory.github.io/?url=https://github.com/ricardocr18/rocketseatCurso_Python/tree/main/nivel3/atividadeProposta).

---

# 🎮 desafioPratico - Chat em Tempo Real

Esta pasta contém o desenvolvimento de uma aplicação de **Chat Multiusuário** com atualização instantânea. O foco deste desafio foi implementar a comunicação bidirecional entre cliente e servidor, permitindo que mensagens sejam enviadas e recebidas sem a necessidade de atualizar a página.

### 🛠️ Funcionalidades Principais
* **Comunicação Bidirecional:** Utilização de WebSockets para troca de mensagens instantâneas.
* **Interface Dinâmica:** Identificação de usuários e estilização diferenciada para mensagens enviadas e recebidas.
* **Status de Conexão:** Monitoramento em tempo real do estado da conexão com o servidor.

### 🏗️ Estrutura do Projeto
* **`app.py`**: Servidor Flask configurado com Flask-SocketIO para gerenciar os eventos de chat.
* **`templates/index.html`**: Interface do usuário com scripts para manipulação de eventos do lado do cliente.
* **`static/`**: Estilização (CSS) para garantir a legibilidade da conversa.

### 💬 Demonstração da Comunicação (Socket.IO)
Abaixo, é possível observar a aplicação rodando em duas instâncias diferentes do navegador, simulando a interação em tempo real entre dois usuários ("Ricardo" e "Pedro"):

<img width="1915" height="1017" alt="Demonstração Chat em Tempo Real" src="https://github.com/user-attachments/assets/8be1b153-63c9-4478-8252-dae02b456c54" />

---

### 📥 Acesso (Download Facilitado)
Para facilitar o acesso, você pode visualizar ou baixar apenas o conteúdo desta pasta:

1. 🚀 **Visualização Rápida:** [Clique aqui para abrir o código no Editor Web](https://github.dev/ricardocr18/rocketseatCurso_Python/tree/main/nivel3/desafioPratico) (Pressione `.` no teclado).
2. 📦 **Download Direto (.zip):** [Clique aqui para baixar apenas esta pasta](https://download-directory.github.io/?url=https://github.com/ricardocr18/rocketseatCurso_Python/tree/main/nivel3/desafioPratico).

---
*Nota: Este repositório faz parte do curso de Python*
