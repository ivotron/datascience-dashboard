import os
from dash import Dash

from app.config import BOOTSTRAP_THEME

from ..Dash_fun import apply_layout_with_auth, load_object, save_object # noqa
from .dash_app import dash_app

dir_path = os.path.dirname(os.path.realpath(__file__))
url_base = "/dash/{}/".format(dir_path.split("/")[-1])


def Add_Dash(server, appbuilder):
    # App Instance
    app = Dash(
        server=server,
        url_base_pathname=url_base,
        external_stylesheets=[BOOTSTRAP_THEME]
    )

    app, layout = dash_app(app)

    apply_layout_with_auth(app, layout, appbuilder)

    return app.server
