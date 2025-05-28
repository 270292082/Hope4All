import sqlite3 as db

DB_PATH = "database/Hope4All.db"

def DB_connection():
    conn = db.connect(DB_PATH)
    conn.row_factory = db.Row
    return conn