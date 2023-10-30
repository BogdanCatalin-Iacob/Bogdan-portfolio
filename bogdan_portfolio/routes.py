'''
App's logic
'''
import json
from flask import render_template
from . import app, mail
from .forms import ContactEmail
from flask_mail import Message


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
    with open('projects.json', 'r', encoding='utf-8') as projects_file:
        apps = json.load(projects_file)

    return render_template('projects.html', apps=apps)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    '''
    Contact form to get in contact by sending email
    '''
    form = ContactEmail()

    msg = Message(
        'Hello',
        sender='bogdancatalin.iacob@gmail.com',
        recipients=['bogdancatalin.iacob@gmail.com'])
    msg.body = 'This is a test email'
    mail.send(msg)
    print('sent')

    return render_template('contact.html', form=form)
