# 🚀 Nível 3 - Comunicação em tempo real com Flask

Bem-vindo ao diretório do **Nível 3**. Este espaço centraliza o aprendizado prático de APIs robustas com Flask e Flask-SocketIO

## 📂 Estrutura do Diretório

1.  **📝 [atividadeProposta](#-atividadeproposta)**: Simulador PIX, plicação back-end em Flask com comunicação em tempo real via SocketIO.
2.  **🎮 [desafioPrático](#-desafiopratico)**:.

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
<img width="600" alt="Tela de Cadastro" src="https://github.com/user-attachments/assets/91cac3c7-88bb-491e-89a3-71ce6c5cafcf" />
<img width="600" alt="Pagamento Realizado" src="https://github.com/user-attachments/assets/15b3c33f-db46-48ec-ab45-ccba43d57633" />

### 📥 Acesso (Download Facilitado)
Para facilitar a visualização ou baixar apenas o conteúdo desta pasta:

1.  🚀 **Visualização Rápida:** [Clique aqui para abrir o código no Editor Web](https://github.dev/ricardocr18/rocketseatCurso_Python/tree/main/nivel3/atividadeProposta) (Pressione `.` no teclado).
2.  📦 **Download Direto (.zip):** [Clique aqui para baixar apenas esta pasta](https://download-directory.github.io/?url=https://github.com/ricardocr18/rocketseatCurso_Python/tree/main/nivel3/atividadeProposta).

---

# 🎮 desafioPratico
O projeto **RetroGame** é um assistente de IA focado na experiência de usuários colecionadores de consoles antigos (80s e 90s).

### 📄 Arquivos de Configuração
* **`retroGame.pdf`**: Documento de Produto (Grounding). Contém o catálogo de consoles, tabela de preços e regras de carência.
* **`assistenteRetroGame.pdf`**: Engenharia de Prompt. Define a persona, regras de concisão e protocolos anti-leak.

---

## 🛠️ Tecnologias e Técnicas Utilizadas
* **Back-end:** Python, Flask, Flask-SQLAlchemy, Flask-SocketIO.
* **IA Generativa:** Engenharia de Prompt (Few-Shot, Zero-Shot), Grounding em PDFs.

## 🚀 Como Executar o Nível 3
* **Scripts Python:** Siga as instruções de instalação na seção `#atividadeProposta`.
* **Assistente de IA:** Carregue os PDFs da pasta `#desafioPratico` no **NotebookLM**.

---
*Nota: Este repositório faz parte da Pós-Graduação em IA Generativa e Alta Performance.*
