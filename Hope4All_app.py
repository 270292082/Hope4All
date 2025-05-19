from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = "Hope4All"
DB_path = 'Database/Hope4All.db'

#users = {} #db replaced

def DB_connection():
    conn = sqlite3.connect(DB_path)
    conn.row_factory = sqlite3.Row
    return conn

#home page
@app.route('/')
def homepage():
    return render_template("homepage.html") #to change for home page

#login
@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get['email']
        password = request.form.get['password']

        conn = DB_connection()
        user = conn.execute("SELECT * FROM Rescuer WHERE Email = ?", (email,)).fetchone()
        conn.close()

        if user:
            if user['Password'] == password:
                session['user_email'] = email
                flash('Login Successful', 'success')
                return redirect(url_for('homepage'))
            else:
                flash("Incorrect email or password. Please try again.", 'error')

        else:
            flash('Account not found. Please register.', 'error')
            return redirect(url_for('login'))
    
    return render_template('loginpage.html')

#account register
@app.route('/register', methods = ['POST', 'GET'])
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

#logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash ('Logged out successfully')
    return redirect(url_for('homepage'))

#report- prevent from reporting
@app.route('/report')
def report():
    if 'user_email' not in session:
        flash('Please login to respond to this report.', 'error')
        redirect(url_for('login'))
    return "<h2>Login to report</h2>"

if __name__ == '__main__':
    app.run(debug=True)