import sqlite3 as db
import base64 

DB_PATH = "database/Hope4All.db"


def db_connection():
    conn = db.connect(DB_PATH)
    conn.row_factory = db.Row
    return conn


def getMissing(MID = ''):
    con = db_connection()
    cur = con.cursor()
    if MID != '':
        cur.execute("SELECT * FROM Missing WHERE MID=?", (MID,))
    else:
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


def get_image(MID):
    con = db.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT ProfilePicture FROM Missing WHERE MID == ?", (MID,))
    image = cur.fetchone()
    cur.close()
    con.close()
    if image != ('',) and image != ('BLOB',):
    #if image and image[0] is not None:
        return base64.b64encode(image[0]).decode('utf-8')
    return None


def getMissingInfo(MID):
    con = db.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT * FROM Missing WHERE MID == ?", (MID,))
    missing = cur.fetchone()
    cur.close()
    con.close()
    return missing
