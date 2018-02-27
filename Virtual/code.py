import sqlite3
from sqlite3 import Error

# [Main]
# Nhận số lượng sản phẩm
def lay_code(slsp):
    database = 'datacode.db'
    idmax = countx(database)
    conn = ketnoi(database)
    with conn :
        if (check_tr(conn,idmax)):
            pha_tr(conn,idmax)
            max_trust = idmax
        else:
            mx_trust = check_max(conn,idmax)
    	


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
        sql = ''' SELECT * FROM CodeG WHERE ID=(SELECT MAX(id) from CodeG)'''
        cur = conn.cursor()
        x = cur.execute(sql).fetchone()
        return int(x[0])

# Check tất cả code
def check_tr(conn,idmax):
    tr = True
    for i in range (idmax+1):
        sql = ''' SELECT * FROM CodeG WHERE id=? '''
        cur = conn.cursor()
        check = cur.execute(sql,(idmax,)).fetchone()
        if check[2]:
            trinh = False
    return tr

# Đánh dấu fisrt
def pha_tr(conn,idmax):
    sql = ''' UPDATE CodeG
              SET Use = ?
              WHERE ID = ?'''
    cur = conn.cursor()
    cur.execute(sql,('1',idmax,))

# Check code chưa dùng
def check_max(conn,idmax):
    sql = ''' SELECT * FROM CodeG WHERE id=? '''
    cur = conn.cursor()
    x = cur.execute(sql,(idmax,)).fetchone()
    # Điều kiện check ở đây
    if not x[2]:
        idmax -= 1
        check_max(conn,idmax)
    else:
        return idmax
    return check_max(conn,idmax)

# Count x for y	
def get_code(slsp,mx_trust):
    pass




