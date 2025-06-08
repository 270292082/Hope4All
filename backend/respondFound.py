from flask import Flask, session, render_template, request, flash, redirect, url_for
from backend.env import *

def found(MID):
    #check user login
    if 'userEmail' not in session:
        #save current page url before redirecting to login
        session['next'] = url_for('RF_found', MID = MID)

        flash("Please log in to respond to this report.", 'error')
        return redirect(url_for('LP_login'))

    conn = db_connection()
    missingPerson = conn.execute('SELECT * FROM Missing WHERE MID = ?', (MID,)).fetchone()
    print(missingPerson)
    rescuer = conn.execute('SELECT * FROM Rescuer WHERE Email = ?', (session['userEmail'],)).fetchone()

    if request.method == 'POST':
        foundLocation =request.form('foundLocation')
        foundDate = request.form('foundDate')
        foundCondition = request.form('foundCondition')
        foundContact = request.form('foundContact')

        reporterName = rescuer['FullName'] 
        reporterRole = rescuer['Role'] 
        RId = rescuer['RID']

        conn.execute(
            'INSERT INTO Reports (RID, MID, FoundLocation, FoundDate, FoundCondition, FoundContact) VALUES (?,?,?,?,?,?)',
            (RId, MID, foundLocation, foundDate, foundCondition, foundContact)
        )
        conn.commit()
        conn.close()
        flash('Report submitted successfully.')
        return redirect(url_for('homepage'))
    
    conn.close()
    return render_template('respondfound.html', missingPerson = missingPerson, rescuer = rescuer)
