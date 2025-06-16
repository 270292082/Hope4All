from flask import session, render_template, request, flash, redirect, url_for
from backend.env import *
from backend.missingPerson import get_image 

def found(MID):
    #check user login
    if 'userEmail' not in session:
        #save current page url before redirecting to login
        session['next'] = url_for('RF_found', MID = MID)

        flash("Please log in to respond to this report.", 'error')
        return redirect(url_for('LP_login'))

    conn = db_connection()
    missingPerson = conn.execute('SELECT * FROM Missing WHERE MID = ?', (MID,)).fetchone()
    rescuer = conn.execute('SELECT * FROM Rescuer WHERE Email = ?', (session['userEmail'],)).fetchone()

    if request.method == 'POST':
        foundLocation = request.form['foundLocation']
        foundDate = request.form['foundDate']
        foundCondition = request.form['foundCondition']
        foundContact = request.form['foundContact']

        reporterName = rescuer['FirstName'] + " " + rescuer["LastName"] 
        reporterRole = rescuer['Role'] 
        RId = rescuer['RID']

        conn.execute(
            'INSERT INTO Reports (RID, MID, FoundLocation, FoundDate, FoundCondition, FoundContact) VALUES (?,?,?,?,?,?)',
            (RId, MID, foundLocation, foundDate, foundCondition, foundContact)
        )
        conn.commit()
        conn.close()
        #flash('Report submitted successfully.')
        return redirect('/')
    
    conn.close()

    image = get_image(missingPerson['MID'])

    return render_template('respond-found.html', missingPerson = missingPerson, image=image, rescuer = rescuer)
