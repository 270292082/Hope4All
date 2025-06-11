from flask import render_template, request
from backend.env import *

def index(MID):
    missingPerson = getMissingInfo(MID)
    image = get_image(MID)
    return render_template('missing-person.html', missingPerson=missingPerson, image=image)
