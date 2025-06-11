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

def getNotFound():
    con = db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM Missing m LEFT JOIN Reports r ON m.MID = r.MID WHERE r.MID IS NULL;")
    not_founds = cur.fetchall()
    cur.close()
    con.close()
    return not_founds
