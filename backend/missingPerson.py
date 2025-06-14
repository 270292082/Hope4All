from flask import render_template, request
from backend.env import *

import sqlite3

def index(MID):
    # to check if there is already a response for this missing person
    conn = db_connection()
    conn.row_factory = sqlite3.Row
    report = conn.execute(
        "SELECT * FROM Reports WHERE MID = ?", (MID,)
    ).fetchone()

    if report:
        display = conn.execute(
            "SELECT r.*, m.ProfilePicture, m.FirstName, m.LastName, m.Age, m.IdentificationMark, m.Country, m.IncidentRelated FROM Reports r JOIN Missing m ON r.MID = m.MID WHERE r.MID = ?", (MID,)
        ).fetchone()

        conn.close()
        return render_template('after-response.html', report = display)
    
    else:
        missingPerson = getMissingInfo(MID)
        image = get_image(MID)
        return render_template('missing-person.html', missingPerson=missingPerson, image=image)
