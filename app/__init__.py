import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

from app.index import MyIndexView

"""
 Logging configuration
"""
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)


app = Flask(__name__)

app.config.from_object("app.config")

db = SQLA(app)

appbuilder = AppBuilder(app, db.session, indexview=MyIndexView, base_template='mybase.html')

##############################################################################

# Dash_App1 section

from .dashboard.Dash_App1 import Dash_App1

app = Dash_App1.Add_Dash(app, appbuilder)

##############################################################################

# Dash_App2 section

from .dashboard.Dash_App2 import Dash_App2

app = Dash_App2.Add_Dash(app, appbuilder)

##############################################################################



from . import views  # noqa
