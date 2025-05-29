from flask import request, session, flash, redirect, url_for, render_template
import sqlite3 as db
from backend.env import *

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        conn = DB_connection()
        user = conn.execute("SELECT * FROM Rescuer WHERE email = ?", (email,)).fetchone()
        conn.close()

        if user:
            if user['Password'] == password:
                session['userEmail'] = email
                flash('Login Successful', 'success')
                #return redirect(url_for('homepage'))

                # redirect to last accessed page
                nextPage = session.pop('next', None)
                return redirect(nextPage) if nextPage else redirect(url_for('homepage'))
            

            else:
                flash("Incorrect email or password. Please try again.", 'error')

        else:
            flash('Account not found. Please register.', 'error')
            return redirect(url_for('login'))
    
    return render_template('login-page.html')


def register():
    if request.method == 'POST':
        email = request.form['email']
        fullname = request.form['fullname']
        dob = request.form['dob']
        contact = request.form['contact']
        role = request.form['role']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Passwords do not match.", 'error')
            return redirect(url_for('register'))
        
        conn = DB_connection()
        existUser = conn.execute('SELECT * FROM Rescuer WHERE Email = ?', (email,)).fetchone()

        if existUser:
            flash("This email has an existing account.", 'error')
            conn.close()
            return redirect(url_for('login'))
        
        conn.execute(
            'INSERT INTO Rescuer (FullName, DOB, Contact, Role, Email, Password) VALUES (?,?,?,?,?,?)', (fullname, dob, contact, role, email, password)
        )
        conn.commit()
        conn.close()

        flash("Registration Successful. Please proceed to login.", 'success')
        return redirect(url_for('login'))
    
    return render_template('registerpage.html')


def logout():
    session.pop('user', None)
    flash ('Logged out successfully')
    return redirect(url_for('homepage'))