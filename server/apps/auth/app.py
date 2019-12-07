"""
    Blueprint for the authentication logic. This example implements GitHub OAuth.
    For more info on OAuth, refer to [1]. For specifics on the GitHub OAuth process, 
    refer to [2].

    [1]: https://oauth.net/2/
    [2]: https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/
"""

from server import app
from flask import Blueprint, redirect, request
import requests

auth = Blueprint('auth', __name__)

## GET /login
# Redirects user to GitHub OAuth authorize page
@auth.route('/login')
def login():
    client_id = app.config["GITHUB_CLIENT_ID"]
    return redirect("https://github.com/login/oauth/authorize?client_id=%s&redirect_uri=%s/auth/verify" % (client_id, app.config["SERVER_URL"]))

## GET /verify
# Verifies the user using the access code. This is the redirect URI for the GitHub
# OAuth process after authorization. Returns user to main site.
@auth.route('/verify')
def verify():
    try:
        code = request.args.get('code')

        client_id = app.config["GITHUB_CLIENT_ID"]
        client_secret = app.config["GITHUB_CLIENT_SECRET"]

        # Exchange code for access token
        # POST http(s)://[hostname]/login/oauth/access_token
        r = requests.post('https://github.com/login/oauth/access_token', data = {'client_id': client_id, 'client_secret': client_secret, 'code': code})
        response = r.text
        access_token = response.split('&')[0].split('=')[1]
        
        return redirect(app.config["LOGIN_SUCCESS"] + "?access_token=%s" % access_token)
    except Exception:
        return redirect(app.config["LOGIN_ERROR"])