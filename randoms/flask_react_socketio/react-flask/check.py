import socketio
import json

sio = socketio.Client()

# @sio.event
# def connect():
#     print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

@sio.on('connect')
def on_connect(*args):
    for arg in args:
        print(arg)

@sio.on('data')
def on_message(*args):
    for arg in args:
        print(arg)

if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    #sio.wait()
    while True:
        message = input('Enter message: ')
        sio.emit('data', {'dataza': message})