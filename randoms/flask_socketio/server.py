from flask import Flask,request,jsonify
from flask_socketio import SocketIO,emit
from flask_cors import CORS

"""
    This file is the main file of the server.
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/http-call')
def http_call():

    """
        Sends a json verification
    """

    data = {'status': 'request received'}
    return jsonify(data)

@socketio.on('connect')
def connected():
    """ listens to client connection to server """

    print(request.sid, 'connected')
    emit('connect', {'data': f'id: {request.sid} has Connected!'},broadcast=True)

@socketio.on('disconnect')
def disconnected():
    """ listens to client disconnection from server """

    print(request.sid, 'disconnected')
    emit('disconnect', {'data': f'id: {request.sid} has Disconnected!'})

@socketio.on('data')
def handle_message(data):
    """broadcast message to everyone"""
    print('received message: ' + str(data))
    emit('data', {'received data':data}, skip_sid=request.sid, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)


