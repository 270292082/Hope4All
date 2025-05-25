from flask import Flask, request, render_template
import sqlite3 as db
import time

from random import randint, seed

app = Flask(__name__)
db_name = "Database/Hope4All.db"



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reportMissing')
def reportMissing():
    return render_template('reportMissing.html')

    
@app.route('/reportMissing/submit', methods=["GET","POST"])
def db_register():

    if request.method == 'POST':
        # Adding the double check after the random generated number if MID already exist in the database.
        MID = randint(111111111,999999999)
        result = [MID]

        # Check if the generated ID already exists in the database.
        while result[0] == MID:
            seed(time.time())
            MID = randint(111111111,999999999)
            con = db.connect(db_name)
            con.row_factory = db.Row
            cur = con.cursor()
            cur.execute("SELECT MID FROM Missing WHERE MID==?", (MID,))
            result = cur.fetchone()
            if result == None:
                break
            con.close()

        try:
            info = get_inputs()
            with db.connect(db_name) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Missing (MID, FirstName, LastName, Age, IdentificationMark, Contact, MissingSince, LastKnownLocation, IncidentRelated, Country, Additional, ReporterName, ReporterRelation) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (MID, info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9],info[10], info[11]))
                con.commit()
                msg = "Successfully commited!"
        except:
            msg = "ERROR in Operation!"
            con.rollback()

        finally:
            con.close()
            return msg


def get_inputs() -> list:
    info = []
    name = request.form['iname']
    name = name.split()
    firstName = name[0] 
    lastName = name[1]
    info.append(firstName)
    info.append(lastName)
    info.append(request.form['iage'])
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
    return info

if __name__ == '__main__':
    app.run(debug=True)
