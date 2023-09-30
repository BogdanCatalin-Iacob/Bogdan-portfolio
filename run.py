'''
App run module
'''
import os
from bogdan_portfolio import app


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=os.environ.get('DEBUG')
    )
