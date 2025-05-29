import sqlite3 as db

DB_PATH = "database/Hope4All.db"

def db_connection():
    conn = db.connect(DB_PATH)
    conn.row_factory = db.Row
    return conn


def getMissing():
    con = db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM Missing")
    missings = cur.fetchall()
    cur.close()
    con.close()
    return missings