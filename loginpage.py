from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "Hope4All"

#replace with database #Hope4All.db
users = {} 

@app.route('/')
def homepage():
    user = session.get('user') #get user from session if logged in, else none
    return render_template("homepage.html", user = user) #to change for home page

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in users:
            # email exists
            if users[email] == password:
                #flash('Login successful!')
                session['user'] = email
            else:
                flash('Incorrect password. Please try again.')
        
        else:
            #email not exist - create one
            users[email] = password
            session['user'] = email
            #flash("Account created successfully!")
        
        return redirect(url_for('homepage')) 
    
    return render_template('loginpage.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash ('Logged out successfully')
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True)