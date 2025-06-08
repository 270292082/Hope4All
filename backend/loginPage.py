from flask import request, session, flash, redirect, url_for, render_template
import sqlite3 as db
from backend.env import *

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        conn = db_connection()
        user = conn.execute("SELECT * FROM Rescuer WHERE email = ?", (email,)).fetchone()
        conn.close()

        if user:
            if user['Password'] == password:
                session['userEmail'] = email
                flash('Login Successful', 'success')
                #return redirect(url_for('homepage'))

                # redirect to last accessed page
                nextPage = session.pop('next', None)
                return redirect(nextPage) if nextPage else redirect('/homepage')
            

            else:
                flash("Incorrect email or password. Please try again.", 'error')

        else:
            flash('Account not found. Please register.', 'error')
            return redirect('/login')
    
    return render_template('login-page.html')


def register():
    if request.method == 'POST':
        email = request.form['email']
        fname = request.form['firstname']
        lname = request.form['lastname']
        dob = request.form['dob']
        contact = request.form['contact']
        role = request.form['role']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        #if len(name) < 2:
            #flash("Please enter your first name and last name!", 'error')
            #return redirect(url_for('LP_register'))

        if password != confirm_password:
            flash("Passwords do not match.", 'error')
            return redirect('/register')
        
        conn = db_connection()
        existUser = conn.execute('SELECT * FROM Rescuer WHERE Email = ?', (email,)).fetchone()

        if existUser:
            flash("This email has an existing account.", 'error')
            conn.close()
            return redirect('/login')
        
        conn.execute(
            'INSERT INTO Rescuer (FirstName, LastName, DOB, Contact, Role, Email, Password) VALUES (?,?,?,?,?,?,?)', (fname[0], lname[1], dob, contact, role, email, password)
        )
        conn.commit()
        conn.close()

        flash("Registration Successful. Please proceed to login.", 'success')
        return redirect('/login')
    
    return render_template('register-page.html')


def logout():
    session.pop('user', None)
    flash ('Logged out successfully')
    return redirect('/homepage')