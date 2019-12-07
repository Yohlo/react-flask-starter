"""
    A file for function decorators that would be needed for certain flask requests. 
    For more, refer to the flask decorators documentation [1].

    [1]: https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
"""
from functools import wraps
from flask import g, request
import requests

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """
            Specifies that a GitHub authentication token is needed for a specific request.
            If provided, it will load the relative user info (from github's api) into flask.g ([1])

            For more info on the user request being made, see [2].

            [1]: https://flask.palletsprojects.com/en/1.1.x/api/#flask.g
            [2]: https://developer.github.com/v3/users/#get-the-authenticated-user
        """
        # grabs the code from the query parameters
        code = request.args.get('access_token')
        if not code:
            return "No access code given", 400

        # make the request specified in [2]
        r = requests.get("https://api.github.com/user?access_token=%s" % code)
        if not r.status_code == requests.codes.ok:
            return "Issue retrieving user based on given access code. If problem persists, try deleting browser cookies.", r.status_code
        # store in the application context. 
        g.user = r.json()
        return f(*args, **kwargs)
    return decorated_function