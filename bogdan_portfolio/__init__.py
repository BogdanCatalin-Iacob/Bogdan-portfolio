'''
App initialization
'''
import os
from flask import Flask

if os.path.exists('env.py'):
    import env  # noqa

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# rely on app to be defined
from . import routes  # noqa
