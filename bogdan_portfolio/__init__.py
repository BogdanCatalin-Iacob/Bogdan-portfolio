'''
App initialization
'''
import os
from flask import Flask
from flask_mail import Mail

if os.path.exists('env.py'):
    import env  # noqa

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_SSL'] = bool(os.environ.get('MAIL_USE_SSL'))

# create mail app
mail = Mail(app)

# rely on app to be defined
from . import routes  # noqa
