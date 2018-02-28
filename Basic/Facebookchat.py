import time,random
from fbchat import Client
from fbchat.models import *
client = Client('acc', 'pass')
if not client.isLoggedIn():
    client.login('acc', 'pass')

def countdown(t,x):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    client.send(Message(text=x), thread_id='100000415757550', thread_type=ThreadType.USER)

for i in range(200):
    y = ''
    x = random.sample(('anh', 'Anh', 'aNh', 'anH', 'AnH', 'ANH', 'ANh'), 1) + random.sample(
        ('xin', 'Xin', 'XIn', 'XIN', 'XiN', 'xIN', 'xIn'), 1) + random.sample(
        ('lỗi', 'Lỗi', 'lỖi', 'LỗI', 'LỖi', 'lỖI', 'LỗI'), 1) + random.sample(('nha','nHa','nhA','NHA','Nha','nHA'),1)
    for j in range(len(x)):
        y = y + ' ' + x[j]
    countdown(5, y)
