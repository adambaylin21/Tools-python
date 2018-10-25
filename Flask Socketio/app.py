from flask import Flask
from flask_socketio import SocketIO ,send

app = Flask(__name__)
app.config ['SECRET_KEY'] = 'lualenloploplaluanepvang'
socketio = SocketIO(app)

@socketio.on('message')
def handx(msg):
    print('Messenger:',msg)
    if msg == 'nguoidungdaclick':
        print('Trò chơi bắt đầu')
    send(msg, broadcast=False)


if __name__ == '__main__':
    socketio.run(app)