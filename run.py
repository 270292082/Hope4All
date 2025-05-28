from flask import Flask, request, render_template
import sqlite3 as db
import backend.reportMissing as reportMissing

from random import randint, seed

app = Flask(__name__)
db_name = "database/Hope4All.db"


@app.route('/')
def index():
    return render_template('index.html')


# -- Report Missing Page --
@app.route('/reportMissing')
def RM_index():
    return reportMissing.index()

@app.route('/reportMissing/submit', methods=["GET","POST"])
def RM_submit():
    return reportMissing.submit()
# ------


if __name__ == '__main__':
    app.run(debug=True)
