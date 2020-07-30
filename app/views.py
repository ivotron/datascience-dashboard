from flask_appbuilder.baseviews import BaseView
from flask_appbuilder import expose, has_access
from . import appbuilder

#############################################################################

# Dash_App1 section

from .dashboard import Dash_App1

class Dash_App1Class(BaseView):
    route_base = "/"

    @has_access
    @expose( "/Dash_App1/" )
    def methoddash(self):
        return self.render_template("dash.html", dash_url=Dash_App1.url_base, appbuilder=appbuilder)


appbuilder.add_view_no_menu(Dash_App1Class())
appbuilder.add_link(
    "Dash_App1", href="/Dash_App1/", icon="fa-list", category="Dashboard", category_icon="fa-list"
)

##############################################################################

# Dash_App2 section

from .dashboard import Dash_App2

class Dash_App2Class(BaseView):
    route_base = "/"

    @has_access
    @expose( "/Dash_App2/" )
    def methoddash(self):
        return self.render_template("dash.html", dash_url=Dash_App2.url_base, appbuilder=appbuilder)


appbuilder.add_view_no_menu(Dash_App2Class())
appbuilder.add_link(
    "Dash_App2", href="/Dash_App2/", icon="fa-list", category="Dashboard", category_icon="fa-list"
)

##############################################################################
