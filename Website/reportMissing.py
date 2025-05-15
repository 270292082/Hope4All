from flask import Flask, request, render_template
import sqlite3 as db

app = Flask(__name__)
db_name = "Database/Hope4All.db"




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reportMissing')
def reportMissing():
    return render_template('reportMissing.html')

@app.route('/reportMissing/submit')
def get_inputs() -> list:

    if request.method == 'POST':
    
        info = []
        info.append(request.form['iname'])
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
    
        return render_template('index.html')
    

def db_register(info: list):
    # Adding THE MID (random generated number)
    # Adding the double check after the random generated number if MID already exist in the database.
    try:
        with db.connect(db_name) as con:
            cur = con.cusor()
            cur.execute("INSERT INTO Missing (MID, FirstName, LastName, Age, IdentificationMark, Contact, MissingSince, LastKnownLocation, IncidentRelated, Country, Additional) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9]))
            con.commit()
            msg = "Successfully commited!"
    except:
        msg = "ERROR in Operation!"

    finally:
        con.close()
        return msg

if __name__ == '__main__':
    app.run(debug=True)