from flask import Flask, request, render_template
import sqlite3 as db
from random import randint, seed

import backend.loginPage as loginPage
import backend.reportMissing as reportMissing
import backend.respondFound as respondFound
import backend.confirmMissing as confirmMissing
import backend.env as env

# THINGS LEFT TO DO
#  Make the database work with the merged branch.

app = Flask(__name__)
app.secret_key = 'SECRET KEY'
db_name = "database/Hope4All.db"


@app.route('/')
def index():
    return render_template('index.html', missings=env.getMissing())



# -- Login Page --
@app.route('/login', methods=['GET', 'POST'])
def LP_login():
    return loginPage.login()

@app.route('/register', methods = ['POST', 'GET'])
def LP_register():
    return loginPage.register()

@app.route('/logout')
def LP_logout():
    return loginPage.logout()
# ------
 


# -- Report Missing Page --
@app.route('/reportMissing')
def RM_index():
    return reportMissing.index()

@app.route('/reportMissing/submit', methods=["GET","POST"])
def RM_submit():
    return reportMissing.submit()
# ------


# -- Confirm Missing Person Page --
@app.route('/confirm/<int:MID>')
def CM_confirm(MID):
    return confirmMissing.confirm(MID)
# -----



# -- Respond Found Page --
@app.route('/respond/<int:MID>', methods = ['GET', 'POST'])
def RF_found(MID): 
    respondFound.found(MID)
# ------


if __name__ == '__main__':
    app.run(debug=True)