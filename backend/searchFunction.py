from flask import Flask, render_template, request
import sqlite3 as db
from backend.env import *

from flask import jsonify

def search():
    query = request.args.get('query','').strip().lower()
    results = []

    if query:
        conn = db_connection()
        conn.row_factory = db.Row

        # allow fullname, firstname, lastname, age and partial name search
        results = conn.execute(
            "SELECT MID, FirstName, LastName, Age, IdentificationMark, Contact from Missing WHERE LOWER(FirstName) LIKE ? OR LOWER(LastName) LIKE ? OR LOWER(FirstName || ' ' || LastName) LIKE ? OR Age = ?",
            (f"%{query}%", f"%{query}%", f"%{query}%", query if query.isdigit() else -1)
        ).fetchall()
        conn.close()

    return render_template('search-results.html', missings = [], search_results = results, search_term = query)


def search_json():
    query = request.args.get('query','').strip().lower()
    results = []

    if query:
        conn = db_connection()
        conn.row_factory = db.Row

        # allow fullname, firstname, lastname, age and partial name search
        db_results = conn.execute(
            "SELECT MID, FirstName, LastName, Age, IdentificationMark, Contact from Missing WHERE LOWER(FirstName) LIKE ? OR LOWER(LastName) LIKE ? OR LOWER(FirstName || ' ' || LastName) LIKE ? OR Age = ?",
            (f"%{query}%", f"%{query}%", f"%{query}%", query if query.isdigit() else -1)
        ).fetchall()
        conn.close()

        results = [
            {
                "MID" : row["MID"],
                "FirstName" : row["FirstName"],
                "LastName" : row["LastName"],
                "Age" : row["Age"]
            } for row in db_results
        ]
    return jsonify(results)