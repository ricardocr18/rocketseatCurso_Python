from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' # Necessário para sessões do SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    sid = request.sid
    print(f'Client connected: {sid}')

@socketio.on('message')
def handle_message(msg):
    msg['sid'] = request.sid
    emit('message', msg, broadcast=True, include_self=False)
    print(f'Message: {msg}')

@socketio.on('disconnect')
def on_disconnect():
    sid = request.sid
    print(f'Client disconnected: {sid}')

if __name__ == '__main__':
    socketio.run(app, debug=True)
