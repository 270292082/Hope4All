from flask import request, render_template, redirect, flash
from random import seed, randint
from datetime import datetime
import time
import sqlite3 as db
from backend.env import *

def index():
    return render_template('report-missing.html')

def submit():

    if request.method == 'POST':
        # Adding the double check after the random generated number if MID already exist in the database.
        MID = randint(111111111,999999999)
        result = [MID]

        # Check if the generated ID already exists in the database.
        while result[0] == MID:
            seed(time.time())
            MID = randint(111111111,999999999)
            con = db.connect(DB_PATH)
            con.row_factory = db.Row
            cur = con.cursor()
            cur.execute("SELECT MID FROM Missing WHERE MID==?", (MID,))
            result = cur.fetchone()
            if result == None:
                break
            con.close()

        try:
            info = get_inputs()
            with db.connect(DB_PATH) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Missing (MID, FirstName, LastName, DOB, Age, IdentificationMark, Contact, MissingSince, IncidentRelated, LastKnownLocation, Country, ReporterName, ReporterRelation, Additional, ProfilePicture) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (MID, info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9],info[10], info[11], info[12], info[13]))
                con.commit()
                flash("Successfully commited!")

        except:
            flash("ERROR in operation!")
            con.rollback()

        finally:
            con.close()
            return redirect('/')

def get_inputs() -> list:
    info = []
    name = request.form['iname']
    name = name.split()
    if len(name) < 2:
        firstName = name[0]
        lastName = ""
    else:
        firstName = name[0] 
        lastName = name[1]

    info.append(firstName)
    info.append(lastName)
    info.append(request.form['idob'])

    # Calculate the Age.
    dob = datetime.strptime(info[-1], "%d/%m/%Y").date()
    today = datetime.today().date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) 
    info.append(age)

    info.append(request.form['iidmark'])
    info.append(request.form['icontact'])
    info.append(request.form['imissdate'])
    info.append(request.form['irelated'])
    info.append(request.form['ilastlocation'])
    info.append(request.form['icountry'])
    info.append(request.form['ireportername'])
    info.append(request.form['irelation'])
    info.append(request.form['inotes'])
    print(info)
    file = request.files['ipp']
    if file:
        image_data = file.read()
        mimetype = file.mimetype
        info.append(image_data)
    else:
        info.append('')
    return info