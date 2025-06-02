from flask import Flask, render_template, url_for, request
import sqlite3 as db
from backend.env import *

def confirm(MID):
    conn = db_connection()
    conn.row_factory = db.Row
    missingPerson = conn.execute("SELECT * FROM Missing WHERE MID = ?", (MID,)).fetchone()
    conn.close()

    if not missingPerson:
        return "Missing Person not found.",404
    return render_template('confirm-missing.html', missingPerson = missingPerson)