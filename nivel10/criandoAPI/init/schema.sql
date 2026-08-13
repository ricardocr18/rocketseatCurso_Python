-- Criação da tabela "users"

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usr_name TEXT NOT NULL,
    age INTEGER,
    uf TEXT        
);