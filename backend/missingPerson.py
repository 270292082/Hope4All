from flask import Flask, render_template, request
import sqlite3
import base64

from backend.env import *

def index(MID):
    missingPerson = get_info(MID)
    image = get_image(MID)
    print(image)
    return render_template('missing-person.html', missingPerson=missingPerson, image=image)

def get_info(MID):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT * FROM Missing WHERE MID == ?", (MID,))
    missing = cur.fetchone()
    cur.close()
    con.close()
    return missing

def get_image(MID):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT ProfilePicture FROM Missing WHERE MID == ?", (MID,))
    image = cur.fetchone()
    cur.close()
    con.close()
    if image != ('',) and image != ('BLOB',):
        return base64.b64encode(image[0]).decode('utf-8')
    return None
