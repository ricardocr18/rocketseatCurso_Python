from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "login"

# recuperar usuário pelo ID, função obrigatória do flask-login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rota de Login
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first() # Buscar usuário no banco de dados

        if user and user.password == password:
            login_user(user)
            print(f"Aqui Está o Resultado, {current_user.is_authenticated}")
            return jsonify({"message": "Credenciais estão ok, você está Logado no Sistema!!!"}), 200

    return jsonify({"message": "Credenciais invalidas"}), 400

# Sair da aplicação, fazer o Logout
@app.route("/logout", methods=["GET"])
def logout():
    if not current_user.is_authenticated:
        return jsonify({"message": "Você já está deslogado do sistema"})
    
    logout_user()
    return jsonify({"message": "Logout, realizado com sucesso"})

#Cadastrar usuário
@app.route("/user", methods=["POST"])
def create_user():
    data = request.json # pegar os dados do corpo da requisição
    username = data.get("username")
    password = data.get("password")

    # Verificar se os dados são válidos
    if username and password:
        if User.query.filter_by(username=username).first(): # Verificar se o usuário já existe
            return jsonify({"message": "Usuário já existe"}), 400

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Usuário criado com sucesso"}), 201

    return jsonify({"message": "Dados inválidos"}), 400

# Recuperar o usuário pelo id
@app.route("/user/<int:user_id>", methods=["GET"])
def read_user(user_id):
    # Primeiro verifica se está autenticado
    if not current_user.is_authenticated:
            return jsonify({"message": "Autenticação necessária no sistema"}), 401

    user = User.query.get(user_id)
    if user: 
        return jsonify({"id": user.id, "username": user.username}), 200
    return jsonify({"message": "Usuário não encontrado"}), 404

# Fazer o upgade do dados
@app.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    # Primeiro verifica se está autenticado
    if not current_user.is_authenticated:
            return jsonify({"message": "Autenticação necessária no sistema"}), 401

    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.get(user_id)
    if user:
        if username:
            user.username = username
        if password:
            user.password = password
        db.session.commit()
        return jsonify({"message": "Usuário atualizado com sucesso"}), 200

    return jsonify({"message": "Usuário não encontrado"}), 404


# Deletar usuário
@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    # Primeiro verifica se está autenticado
    if not current_user.is_authenticated:
            return jsonify({"message": "Autenticação necessária no sistema, para deletar conta"}), 401
    
    if current_user.id == user_id:
         return jsonify({"message": "Usuário não pode deletar sua própria conta enquanto está logado"}), 400

    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Usuário deletado com sucesso"}), 200

    return jsonify({"message": "Usuário não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)