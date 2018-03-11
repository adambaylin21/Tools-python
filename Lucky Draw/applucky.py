from flask import Flask , render_template
from flask_socketio import SocketIO ,send
from getlucky import *

appsock = Flask(__name__)
appsock.config ['SECRET_KEY'] = 'lualenloploplaluanepvang'
socketio = SocketIO(appsock)


@socketio.on('message')
def handx(start):
    if stopx(start):
        datadraw = getluckyx('full')
        send(datadraw, broadcast=True)
        print ('Da Sent')
    else :
        print ('Da Dung')

def lkdraw():
    datadraw = getluckyx('full')
    i = random.randint(0, len(datadraw) - 1)
    return (datadraw[i])

def countdown(t,x):
    while t:
        time.sleep(1)
        t -= 1
    i = random.randint(0, len(x) - 1)
    return (x[i])
def stopx(x):
    if x == 'stop':
        return False
    else:
        return True

@appsock.route('/')
def index():
    return render_template('luckydraw.html')

if __name__ == '__main__':
    socketio.run(appsock)
