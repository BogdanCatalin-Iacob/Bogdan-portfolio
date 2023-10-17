'''
Contact by email form
'''
from flask_wtf import FlaskForm
from wtforms import (
    StringField, TextAreaField, SubmitField, EmailField, validators)


class ContactEmail(FlaskForm):
    '''
    Contact form
    '''
    name = StringField('Name', [
        validators.DataRequired('Please, input your name!'),
        validators.Length(min=4, max=25)])
    email = EmailField('Email address', [
        validators.DataRequired(),
        validators.Email()])
    message = TextAreaField('Your message', [
        validators.DataRequired(),
        validators.Length(min=10, max=500)])
    submit = SubmitField('Send')
