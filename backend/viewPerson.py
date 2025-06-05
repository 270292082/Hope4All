from flask import Flask, render_template, request
import sqlite3

def index(missingPerson):
    return render_template('report-missing.html', missingPerson=missingPerson)