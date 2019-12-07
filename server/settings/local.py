"""
    Settings that are to be used in a local development environment.
"""
from .base import *

DEBUG = True
DATABASE_URI = "sqlite:///starter_dev.db"
SERVER_URL = "http://localhost:5000"

## Keys for GitHub OAuth App
GITHUB_CLIENT_ID = ""
GITHUB_CLIENT_SECRET = ""

## Callbacks for authentication
LOGIN_SUCCESS = "http://localhost:3000/OAuth/Success"
LOGIN_ERROR = "http://localhost:3000/OAuth/Error"

print("YOU ARE IN A DEVELOPMENT ENVIRONMENT - YOU SHOULD NOT SEE THIS MESSAGE IN PRODUCTION")