"""
    Using sqlalchemy to connect to the database, create a scoped session
    and connects that to flask. For more, refer to the sqlalchemy documentation [1]
    and the official flask docs for using sqlalchemy [2]

    [1]: https://docs.sqlalchemy.org/en/13/orm/tutorial.html
    [2]: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/
"""
from sqlalchemy import create_engine, event
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from server import app

engine = create_engine(app.config['DATABASE_URI'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

@app.after_request
def after_request(response):
    db_session.remove()
    return response