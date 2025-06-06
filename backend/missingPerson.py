from flask import Flask, render_template, request
import sqlite3

from backend.env import *

def index(MID):
    missingPerson = get_info(MID)
    return render_template('missing-person.html', missingPerson=missingPerson)

def get_info(MID):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT * FROM Missing WHERE MID == ?", (MID,))
    missing = cur.fetchone()
    cur.close()
    con.close()
    return missing
