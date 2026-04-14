from flask import Flask, request, jsonify
from models.user import User
from models.meal import Meal
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "login"

# Adicione este handler para retornar JSON em vez de redirect
@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"message": "Autenticação necessária. Faça login primeiro."}), 401

# recuperar usuário pelo ID, função obrigatória do flask-login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# recuperar usuário pelo ID, função obrigatória do flask-login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ==================== ROTAS DE USUÁRIO ====================

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
        return jsonify({"message": "Você não está logado no sistema"}), 401
    
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
        return jsonify({
             "message": "Usuário criado com sucesso",
             "user": {"id": new_user.id, "username": new_user.username}
        }), 201

    return jsonify({"message": "Dados inválidos"}), 400

# Recuperar o usuário pelo id
@app.route("/user/<int:user_id>", methods=["GET"])
def read_user(user_id):
    # Primeiro verifica se está autenticado
    if not current_user.is_authenticated:
            return jsonify({"message": "Autenticação necessária no sistema"}), 401

    user = User.query.get(user_id)
    if user: 
        return jsonify({
             "id": user.id,
             "username": user.username,
             "total_meals": len(user.meals)}), 200    
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


# ==================== ROTAS DE REFEIÇÕES ====================

# Criar refeição
@app.route("/meal", methods=["POST"])
@login_required
def create_meal():
    data = request.json
    
    # Validações
    if not data.get("name"):
        return jsonify({"message": "Nome da refeição é obrigatório"}), 400

    # Processar data/hora
    date_time = datetime.utcnow()
    if data.get("date_time"):
        try:
            date_time = datetime.fromisoformat(data["date_time"].replace('Z', '+00:00'))
        except ValueError:
            return jsonify({"message": "Formato de data inválido. Use ISO 8601: YYYY-MM-DDTHH:MM:SS"}), 400

    # Criar refeição
    new_meal = Meal(
        name=data["name"],
        description=data.get("description", ""),
        date_time=date_time,
        is_on_diet=data.get("is_on_diet", True),
        user_id=current_user.id
    )
    
    db.session.add(new_meal)
    db.session.commit()
    
    return jsonify({
        "message": "Refeição criada com sucesso",
        "meal": new_meal.to_dict()
    }), 201

# Listar todas as refeições do usuário logado
@app.route("/meals", methods=["GET"])
@login_required
def get_meals():
    meals = Meal.query.filter_by(user_id=current_user.id).order_by(Meal.date_time.desc()).all()
    
    return jsonify({
        "meals": [meal.to_dict() for meal in meals],
        "total": len(meals)
    }), 200

# Buscar refeição específica
@app.route("/meal/<int:meal_id>", methods=["GET"])
@login_required
def get_meal(meal_id):
    meal = db.session.get(Meal, meal_id)
    
    if not meal:
        return jsonify({"message": "Refeição não encontrada"}), 404
    
    if meal.user_id != current_user.id:
        return jsonify({"message": "Você não tem permissão para acessar esta refeição"}), 403
    
    return jsonify(meal.to_dict()), 200

# Editar refeição (alterando todos os dados)
@app.route("/meal/<int:meal_id>", methods=["PUT"])
@login_required
def update_meal(meal_id):
    meal = db.session.get(Meal, meal_id)
    
    if not meal:
        return jsonify({"message": "Refeição não encontrada"}), 404
    
    if meal.user_id != current_user.id:
        return jsonify({"message": "Você não tem permissão para editar esta refeição"}), 403
    
    data = request.json
    
    # Atualizar todos os campos
    if "name" in data:
        if not data["name"]:
            return jsonify({"message": "Nome da refeição não pode ser vazio"}), 400
        meal.name = data["name"]
    
    if "description" in data:
        meal.description = data["description"]
    
    if "date_time" in data:
        try:
            meal.date_time = datetime.fromisoformat(data["date_time"].replace('Z', '+00:00'))
        except ValueError:
            return jsonify({"message": "Formato de data inválido"}), 400
    
    if "is_on_diet" in data:
        meal.is_on_diet = bool(data["is_on_diet"])
    
    db.session.commit()
    
    return jsonify({
        "message": "Refeição atualizada com sucesso",
        "meal": meal.to_dict()
    }), 200

# Deletar refeição
@app.route("/meal/<int:meal_id>", methods=["DELETE"])
@login_required
def delete_meal(meal_id):
    meal = db.session.get(Meal, meal_id)
    
    if not meal:
        return jsonify({"message": "Refeição não encontrada"}), 404
    
    if meal.user_id != current_user.id:
        return jsonify({"message": "Você não tem permissão para deletar esta refeição"}), 403
    
    db.session.delete(meal)
    db.session.commit()
    
    return jsonify({"message": "Refeição deletada com sucesso"}), 200

# Buscar usuário e TODAS suas refeições
@app.route("/user/<int:user_id>/meals", methods=["GET"])
@login_required
def get_user_meals(user_id):
    user = db.session.get(User, user_id)
    
    if not user:
        return jsonify({"message": "Usuário não encontrado"}), 404
    
    # Opcional: permitir apenas visualizar próprias refeições
    if current_user.id != user_id:
        return jsonify({"message": "Você só pode ver suas próprias refeições"}), 403
    
    meals = Meal.query.filter_by(user_id=user_id).order_by(Meal.date_time.desc()).all()
    
    return jsonify({
        "user": {
            "id": user.id,
            "username": user.username
        },
        "meals": [meal.to_dict() for meal in meals],
        "total_meals": len(meals)
    }), 200

# Métricas da dieta do usuário
@app.route("/meals/metrics", methods=["GET"])
@login_required
def get_metrics():
    meals = Meal.query.filter_by(user_id=current_user.id).order_by(Meal.date_time).all()
    
    total_meals = len(meals)
    meals_on_diet = sum(1 for meal in meals if meal.is_on_diet)
    meals_off_diet = total_meals - meals_on_diet
    
    # Calcular melhor sequência dentro da dieta
    best_sequence = 0
    current_sequence = 0
    
    for meal in meals:
        if meal.is_on_diet:
            current_sequence += 1
            best_sequence = max(best_sequence, current_sequence)
        else:
            current_sequence = 0
    
    percentage = (meals_on_diet / total_meals * 100) if total_meals > 0 else 0
    
    return jsonify({
        "total_meals": total_meals,
        "meals_on_diet": meals_on_diet,
        "meals_off_diet": meals_off_diet,
        "percentage_on_diet": round(percentage, 2),
        "best_sequence_on_diet": best_sequence
    }), 200

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello, World!"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("✅ Tabelas criadas com sucesso!")
    
    app.run(debug=True)