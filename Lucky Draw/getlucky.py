import sqlite3
from sqlite3 import Error
from ast import literal_eval
import time,random

# [Main]
# Tìm người may mắn
def getluckyx(data):
    database = 'luxuryfan.db'
    conn = ketnoi(database)
    with conn:
        # print ('Tất cả có : %s người chơi ' % maxtrust(conn))
        full = listplay(conn)
        datadraw = fullcode(full)
        # reward(datadraw))
        if data == 'max':
            return ('Tất cả có : %s người chơi ' % maxtrust(conn))
        if data == 'full':
            # print (datadraw)
            for i in range (0,len(datadraw)):
                print (datadraw[i],';',end="")

# Lucky Draw
def reward(data):
    for i in range(1000000):
        countdown(1, data)


# Time count down
def countdown(t, x):
    while t:
        time.sleep(.300)
        t -= 1
    i = random.randint(0, len(x) - 1)
    return (x[i])

# Danh sách quay thưởng
def fullcode(full):
    codef = []
    for i in full:
        j = literal_eval(i[4])
        for y in range(0, len(j)):
            codef.append('Name:%s, Tel:%s, Code:%s' % (i[1], i[2], j[y]))
    return codef

# Danh sách người chơi
def listplay(conn):
    sql = ''' select * from datax '''
    cur = conn.cursor()
    x = cur.execute(sql).fetchall()
    return x

# Có bao nhiêu người chơi ?
def maxtrust(conn):
    sql = ''' select count(*) from datax '''
    cur = conn.cursor()
    x = cur.execute(sql).fetchone()
    return x[0]

# Kết nối database
def ketnoi(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

# Lấy max id
def countx(db_name):
    conn = ketnoi(db_name)
    with conn :
        sql = ''' SELECT * FROM datax WHERE ID=(SELECT MAX(id) from datax)'''
        cur = conn.cursor()
        x = cur.execute(sql).fetchone()
        return int(x[0])
# lấy min id
def min_check(db_name):
    conn = ketnoi(db_name)
    with conn :
        sql = ''' SELECT * FROM datax WHERE ID=(SELECT MIN(id) from datax)'''
        cur = conn.cursor()
        x = cur.execute(sql).fetchone()
        return int(x[0])

if __name__ == "__main__":
    getluckyx("full")