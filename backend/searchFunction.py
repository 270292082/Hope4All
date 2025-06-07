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

        results = conn.execute(
            "SELECT FirstName, LastName, Age from Missing WHERE LOWER(FirstName) LIKE ? OR LOWER(LastName) LIKE ? OR LOWER(FirstName || ' ' || LastName) LIKE ? OR Age = ?",
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

        db_results = conn.execute(
            "SELECT FirstName, LastName, Age from Missing WHERE LOWER(FirstName) LIKE ? OR LOWER(LastName) LIKE ? OR LOWER(FirstName || ' ' || LastName) LIKE ? OR Age = ?",
            (f"%{query}%", f"%{query}%", f"%{query}%", query if query.isdigit() else -1)
        ).fetchall()
        conn.close()

        results = [
            {
                "FirstName" : row["FirstName"],
                "LastName" : row["LastName"],
                "Age" : row["Age"]
            } for row in db_results
        ]
    return jsonify(results)