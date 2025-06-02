from flask import Flask, render_template, request
import sqlite3 as db
from backend.env import *

def search():
    query = request.args.get('query','').strip()
    results = []

    if query:
        conn = db_connection()
        conn.row_factory = db.Row

        results = conn.execute(
            "SELECT FirstName, LastName, Age from Missing WHERE  FirstName LIKE ? OR LastName LIKE ? OR Age = ?",
            (f"%{query}%", f"%{query}%", query if query.isdigit() else -1)
        ).fetchall()
        conn.close()
    
    return render_template('search-results.html', missings = [], search_results = results, search_term = query)