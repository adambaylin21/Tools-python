import sqlite3 , random
from sqlite3 import Error
def ketnoi(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
def create_project(conn, project):
    sql = ''' INSERT INTO CodeG(Code)
                VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql,[project])

def main (code):
    database = 'database.db'
    conn = ketnoi(database)
    with conn :
        create_project(conn, code)

for i in range (1000):
    name = 'Luxury'
    char = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    char2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    code = ('{0}-{1}{2}{3:04}'.format(name, char, char2, i))
    main(code)
    print (code)


# if __name__ == '__main__':
#     main()



