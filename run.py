from server import app as application
from server.database import init_db

if __name__ == "__main__":
    init_db()
    application.run(port=5000)