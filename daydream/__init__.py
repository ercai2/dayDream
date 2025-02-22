from flask import Flask 

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment 

app = Flask('daydream')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True       # ??????
app.jinja_env.lstrip_blocks = True     # ??????


from daydream import views, errors, commands