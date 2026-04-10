from flask import Flask, jsonify, request, send_file, render_template
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timedelta
from payments.pix import Pix
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)
socketio = SocketIO(app)

# Rota que vai permitir que o usuário crie um pagamento via pix
@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()

    if 'value' not in data:
        return jsonify ({"message": "O campo value é obrigatório"}), 400
    
    # pegar data e hora atual, onde o pagamento vai expirar em 30 minutos
    expiration_date  = datetime.now() + timedelta(minutes=30)

    # criar um novo pagamento no banco de dados, onde o campo bank_payment_id e qr_code vão ser preenchidos depois que o pagamento for criado na instituição financeira
    new_payment = Payment(value=data['value'], expiration_date=expiration_date)

    pix_obj = Pix() # criar um objeto da classe Pix
    data_payment_pix = pix_obj.create_payments() # criar o pagamento na instituição financeira, onde vai retornar o bank_payment_id e o caminho do qr_code
    new_payment.bank_payment_id = data_payment_pix['bank_payment_id'] # preencher o campo bank_payment_id do pagamento criado no banco de dados
    new_payment.qr_code = data_payment_pix['qr_code_path'] # preencher o campo qr_code

    # salvando os dados no banco de dados
    db.session.add(new_payment)
    db.session.commit()

    return jsonify ({"message": "O pagamento foi criado via pix",
                     "payment": new_payment.to_dict()}), 201

# Rota para exibir o QR code do pagamento
@app.route('/payments/pix/qr_code/<file_name>', methods=['GET'])
def get_image(file_name):
    return send_file(f'static/img/{file_name}.png', mimetype='image/png')

# Rota que vai nos permitir que a instituição financeira recebeu o pagamento
# aqui será criado o WEBHOOK
@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify ({"message": "O pagamento foi confirmado"})

# rota que vai ermitir que o usuário visualize o pagamento
# a variavel <int:pagament_id> é um parametro que representa o id do pagamento
@app.route('/payments/pix/<int:pagament_id>', methods=['GET'])
def payment_pix_page(pagament_id):
    payment = Payment.query.get(pagament_id) # aqui você pode pegar os dados do pagamento no banco de dados, onde você pode passar esses dados para o template payment.html para exibir as informações do pagamento para o usuário
        
    return render_template('payment.html',
                            payment_id=payment.id,
                            value=payment.value,
                            host="http://127.0.0.1:5000",
                            qr_code=payment.qr_code) # aqui estamos passando os dados do pagamento para o template payment.html, onde o template vai exibir as informações do pagamento para o usuário  

# websockets
@socketio.on('connect')
def handle_connect():
    print('Cliente conectado to the Server')

if __name__ == '__main__':
    socketio.run(app, debug=True)