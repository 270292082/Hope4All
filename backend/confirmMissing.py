from flask import Flask, render_template
import sqlite3 as db
from backend.env import *
from backend.missingPerson import get_image

def confirm(MID):
    conn = db_connection()
    conn.row_factory = db.Row
    missingPerson = conn.execute("SELECT * FROM Missing WHERE MID = ?", (MID,)).fetchone()
    conn.close()

    if not missingPerson:
        return "Missing Person not found.",404

    image = get_image(missingPerson['MID']) 
    return render_template('confirm-missing.html', missingPerson = missingPerson, image=image)