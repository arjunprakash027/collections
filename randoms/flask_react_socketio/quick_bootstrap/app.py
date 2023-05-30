from flask_socketio import *
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")


users = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print("user connected")

@socketio.on('register')
def userAdded(username):
    users.append(username)
    print(username)
    emit('user_registered',{'data':username},broadcast=True)

    
if __name__ == '__main__':
    socketio.run(app, debug=True)