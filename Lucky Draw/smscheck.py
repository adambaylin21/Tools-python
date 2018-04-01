import sqlite3
from sqlite3 import Error
from ast import literal_eval

# [Main]
# Tim nguoi chua gui sms
def smscheck():
    database = 'luxuryfan.db'
    conn = ketnoi(database)
    idmin = min_check(database)
    idmax = countx(database)
    with conn:
        dasent(conn,idmin,idmax)

# Check sms
def dasent(conn,idmin,idmax):
    # x = idmin
    # y = idmax
    sql = ''' SELECT tenkh FROM datax WHERE id=? '''
    cur = conn.cursor()
    while idmin <= idmax:
        check = cur.execute(sql,(idmin,)).fetchone()
        print (check)
        idmin += 1


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
    print (smscheck())