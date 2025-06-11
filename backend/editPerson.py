from flask import render_template, request, redirect, flash
from backend.env import *
import backend.reportMissing as reportMissing

def index(MID):
    missingPerson = getMissing(MID)[0]
    image = get_image(MID)
    return render_template("edit-person.html", missingPerson = missingPerson, image = image)

def submit(MID):
    if request.method == 'POST':
        try:
            info = reportMissing.get_inputs()
            with db.connect(DB_PATH) as con:
                cur = con.cursor()
                cur.execute("UPDATE Missing SET FirstName=?, LastName=?, DOB=?, Age=?, IdentificationMark=?, Contact=?, MissingSince=?, IncidentRelated=?, LastKnownLocation=?, Country=?, ReporterName=?, ReporterRelation=?, Additional=? WHERE MID=?;", (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9], info[10], info[11], info[12], MID)) 
                if info[13] != '':
                    cur.execute("UPDATE Missing SET ProfilePicture=? WHERE MID=?;", (info[13], MID))
                    con.commit()

            flash("Successfully commited!")



        except:
            flash("ERROR in operation!")
            con.rollback()

        finally:
            con.close()
            return redirect('/')