# 🚀 RocketSeat - AtividadeProposta (PIX + SocketIO)

Descrição
---------
Projeto exemplo em Flask + Flask-SocketIO que simula pagamentos via PIX (QR code fictício). Contém back-end, templates e imagens de QR.  

Status
------
- ✅ Funcional em ambiente de desenvolvimento
- ⚠️ Banco local em `instance/database.db`

Pré-requisitos
--------------
- Python 3.10+
- Dependências em `requirements.txt`

Instalação (Windows / PowerShell)
---------------------------------
1. Criar/ativar virtualenv (se necessário):
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependências:
```powershell
pip install -r requirements.txt
```

4. Criar tabelas do banco (gera `instance/database.db` se não existir):
```powershell
python -c "from app import app; from repository.database import db; 
with app.app_context(): db.create_all(); print('tables created')"
```

5. Rodar a aplicação:
```powershell
python app.py
```
A aplicação ficará disponível em: `http://127.0.0.1:5000`

Estrutura principal
-------------------
- `app.py` — rotas + inicialização Flask + SocketIO  
- `db_models/payment.py` — model `Payment`  
- `repository/database.py` — `db = SQLAlchemy()`  
- `instance/database.db` — banco sqlite local 
- `static/` — CSS, imagens, QR codes  
- `templates/` — `payment.html`, `confirmed_payment.html`, `404.html`  

Endpoints importantes
---------------------
- `POST /payments/pix`  
  - Body JSON: `{ "value": 150.0 }`  
  - Retorna: 201 com o objeto `payment` (id, value, bank_payment_id, qr_code, ...)

- `GET /payments/pix/qr_code/<file_name>`  
  - Retorna imagem `static/img/<file_name>.png`

- `POST /payments/pix/confirmation` (webhook simulado)
  - Body JSON (ex.):
  ```json
  {
    "bank_payment_id": "ed5cc771-b2b1-418a-bf61-5eadeb913306",
    "value": 650
  }
  ```
  - Respostas:
    - `200` — pagamento confirmado
    - `400` — dados inválidos
    - `404` — payment not found

- `GET /payments/pix/<int:id>`  
  - Renderiza a página do pagamento (template HTML)

Dicas de uso / testes
---------------------
- No Postman: defina header `Content-Type: application/json`.
- Exemplo curl (criar pagamento):
```bash
curl -X POST http://127.0.0.1:5000/payments/pix \
  -H "Content-Type: application/json" \
  -d '{"value":150.0}'
```
- Exemplo curl (confirmar pagamento):
```bash
curl -X POST http://127.0.0.1:5000/payments/pix/confirmation \
  -H "Content-Type: application/json" \
  -d '{"bank_payment_id":"<id>","value":650}'
```

Banco de dados
--------------
- Arquivo: `instance/database.db`  
- Para inspecionar tabelas (PowerShell):
```powershell
python - <<'PY'
import sqlite3
p="instance/database.db"
conn=sqlite3.connect(p)
print(conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
conn.close()
PY
```
- NÃO comitar: `instance/` e `*.db`.

Sugestão `.gitignore`
---------------------
```







