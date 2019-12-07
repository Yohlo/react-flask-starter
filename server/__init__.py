"""
    Initialize the flask app and all dependecies such as
    blueprints [1] and the dotenv environment [2].

    [1]: https://flask.palletsprojects.com/en/1.1.x/blueprints/
    [2]: https://stackoverflow.com/questions/41546883/can-somebody-explain-the-use-of-python-dotenv-module
"""
import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

_basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# gets the environment variable ENV from our .env and loads in the appropriate settings file
# check out the settings app in this starter code for more info
if os.environ.get("ENV") in ('local', 'dev'):
    # setting up CORS for development environments only
    from flask_cors import CORS
    CORS(app, resources=r'/*', allow_headers='Content-Type')
    app.config.from_object(f'server.settings.{os.environ.get("ENV")}')
else:
    app.config.from_object('server.settings.base')

# registers the site blueprint, which gives access to our React.js app.
# it's important to specify the location of the static files so that flask
# knows to serve those when the react app calls for it.
from server.apps.site.app import site
site.static_folder = f"{_basedir}/../client_app/build/static"
site.static_url_path = f'{app.config["APPLICATION_ROOT"]}/static'
site.template_folder = f"{_basedir}/../client_app/build"
app.register_blueprint(site, url_prefix=f'{app.config["APPLICATION_ROOT"]}/')

# register the auth and api apps. 
from server.apps.auth.app import auth
app.register_blueprint(auth, url_prefix=f'{app.config["APPLICATION_ROOT"]}/auth')

from server.apps.api.app import api
app.register_blueprint(api, url_prefix=f'{app.config["APPLICATION_ROOT"]}/api')