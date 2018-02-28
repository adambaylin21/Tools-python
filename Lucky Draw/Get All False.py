import sqlite3 , random
from sqlite3 import Error
def ketnoi(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
def update_project(conn, Use, IDx):
    sql = ''' UPDATE CodeG
              SET Use = ? 
              WHERE ID = ?'''
    cur = conn.cursor()
    cur.execute(sql,(Use,IDx))

def main (UD):
    database = 'datacode.db'
    conn = ketnoi(database)
    with conn :
        for i in range(countx(database)+1):
            update_project(conn, UD, i)
            i -= 1
        print('Complete !')

def countx(database):
    conn = ketnoi(database)
    with conn :
        sql = ''' SELECT * FROM CodeG WHERE ID=(SELECT MAX(id) from CodeG)'''
        cur = conn.cursor()
        x = cur.execute(sql).fetchone()
        return int(x[0])

x = False
main(x)

