'''
App's logic
'''
import json
from flask import render_template
from . import app


@app.route('/')
def home():
    '''
    Renders home page
    '''
    with open('skills.json', 'r', encoding='utf-8') as skills_file:
        skills = json.load(skills_file)

    return render_template('home.html', skills=skills)


@app.route('/projects')
def projects():
    '''
    Displays created projects
    '''
    return render_template('projects.html')
