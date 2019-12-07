"""
    Settings that are to be used in a development environment.
"""
from .base import *

DEBUG = True
DATABASE_URI = "postgresql://localhost:5432/starter_dev"
SERVER_URL = "https://example.com/dev"
APPLICATION_ROOT="/dev"

## Keys for GitHub IU OAuth App
GITHUB_CLIENT_ID = ""
GITHUB_CLIENT_SECRET = ""

## Callbacks for authentication
LOGIN_SUCCESS = f"{SERVER_URL}/OAuth/Success"
LOGIN_ERROR = f"{SERVER_URL}/OAuth/Error"

print("YOU ARE IN A DEVELOPMENT ENVIRONMENT - YOU SHOULD NOT SEE THIS MESSAGE IN PRODUCTION")