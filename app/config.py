import os
import dash_bootstrap_components as dbc

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

OPENID_PROVIDERS = [
    {"name": "Google", "url": "https://www.google.com/accounts/o8/id"},
    {"name": "Yahoo", "url": "https://me.yahoo.com"},
    {"name": "AOL", "url": "http://openid.aol.com/<username>"},
    {"name": "Flickr", "url": "http://www.flickr.com/<username>"},
    {"name": "MyOpenID", "url": "https://www.myopenid.com"},
]

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
# SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
# SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'
BABEL_DEFAULT_LOCALE = "en"


# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_FOLDER = "translations"
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "es": {"flag": "es", "name": "Spanish"},
    "de": {"flag": "de", "name": "German"},
    "zh": {"flag": "cn", "name": "Chinese"},
    "ru": {"flag": "ru", "name": "Russian"},
}


UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_URL = "/static/uploads/"
AUTH_TYPE = 1
AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"
# APP_NAME = "My App Name"
# APP_ICON = "static/img/logo.jpg"
# APP_THEME = "default.css"  # default
# APP_THEME = "cerulean.css"
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"  # dark theme with visible dropdowns
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
APP_THEME = "slate.css"  # dark gray theme, visible dropdowns
# APP_THEME = "spacelab.css"
# APP_THEME = "united.css"
# APP_THEME = "yeti.css"
# APP_THEME = "superhero.css"
# APP_THEME = "darkly.css"

THEMES = {
    "default.css": dbc.themes.BOOTSTRAP,
    "cerulean.css": dbc.themes.CERULEAN,
    "amelia.css": dbc.themes.BOOTSTRAP,  # no equivalent, sets default
    "cosmo.css": dbc.themes.COSMO,
    "cyborg.css": dbc.themes.CYBORG,
    "flatly.css": dbc.themes.FLATLY,
    "journal.css": dbc.themes.JOURNAL,
    "readable.css": dbc.themes.BOOTSTRAP,  # no equivalent, sets default
    "simplex.css": dbc.themes.SIMPLEX,
    "slate.css": dbc.themes.SLATE,
    "spacelab.css": dbc.themes.SPACELAB,
    "united.css": dbc.themes.UNITED,
    "yeti.css": dbc.themes.YETI,
    "superhero.css": dbc.themes.SUPERHERO,
    "darkly.css": dbc.themes.DARKLY,
}

BOOTSTRAP_THEME = THEMES[APP_THEME]
