from flask import Flask, request, render_template, redirect, url_for
from random import randint, seed

import backend.searchFunction as searchFunction
import backend.loginPage as loginPage
import backend.reportMissing as reportMissing
import backend.respondFound as respondFound
import backend.confirmMissing as confirmMissing
import backend.missingPerson as missingPerson
import backend.editPerson as editPerson
import backend.env as env

# THINGS LEFT TO DO
#  Make the database work with the merged branch.

app = Flask(__name__)
app.secret_key = 'SECRET KEY'
db_name = "database/Hope4All.db"


@app.route('/')
def index():
    not_founds = env.getNotFound()
    images = {}
    for missing in not_founds:
        images[missing['MID']] = missingPerson.get_image(missing['MID'])

    return render_template('index.html', missings = not_founds, images=images)


# -- Search Function --
@app.route('/search', methods = ['GET'])
def search():
    return searchFunction.search()

# search function json
@app.route('/search_json', methods = ['GET'])
def search_json():
    return searchFunction.search_json()
# ------


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

@app.route('/reportMissing/submit', methods = ['GET', 'POST'])
def RM_submit():
    return reportMissing.submit()
# ------

# -- View Missing --
@app.route("/view/<int:MID>")
def MP_index(MID):
    return missingPerson.index(MID)
# ------

# -- Confirm Missing Person Page --
@app.route('/confirm/<int:MID>')
def CM_confirm(MID):
    return confirmMissing.confirm(MID)
# ------


# -- Respond Found Page --
@app.route('/respond/<int:MID>', methods = ['GET', 'POST'])
def RF_found(MID): 
    return respondFound.found(MID)
# ------


# -- Edit Person Page --
@app.route('/edit/<int:MID>')
def EP_index(MID):
    return editPerson.index(MID)

@app.route("/editPerson/submit/<int:MID>", methods = ["POST"])
def EP_submit(MID):
    return editPerson.submit(MID)
# ------



if __name__ == '__main__':
    app.run(debug=True)