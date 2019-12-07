"""
    Flask blueprint that serves a React app. 
"""
from server import app
from flask import Blueprint, render_template

site = Blueprint('site', __name__)

# Handles static files created by the react app
@site.route('/static/<path:path>')
def static_file(path):
    return site.send_static_file(path)

# Render index.html on / and other routes.
@site.route('/', defaults={'path': ''})
@site.route('/<path:path>')
def index(path):
    return render_template('index.html')