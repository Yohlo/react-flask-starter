"""
    Contains all of our base settings. The way this project is set up,
    these are the production settings. 
"""
DEBUG = False

# For a list of all the supported database implementations (dialects),
# please refer to this: https://docs.sqlalchemy.org/en/13/dialects/index.html
DATABASE_URI = "postgresql://localhost:5432/starter"

SERVER_URL = "https://example.com"
APPLICATION_ROOT = ""

## Keys for GitHub OAuth App
GITHUB_CLIENT_ID = ""
GITHUB_CLIENT_SECRET = ""

## Callbacks for authentication
LOGIN_SUCCESS = f"{SERVER_URL}/OAuth/Success"
LOGIN_ERROR = f"{SERVER_URL}/OAuth/Error"