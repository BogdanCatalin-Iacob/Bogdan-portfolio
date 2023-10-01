from flask import render_template
from . import app


@app.route('/')
def home():
    '''
    Renders home page
    '''
    return render_template('base.html')
