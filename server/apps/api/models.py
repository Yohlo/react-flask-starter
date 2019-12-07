"""
    File for main database models live here. This example simply
    stores user accounts with minimal information.

    For more information on schema, see [1]. For information about
    the datatypes available in sqlalchemy, see [2].

    [1]: https://docs.sqlalchemy.org/en/13/orm/tutorial.html#create-a-schema
    [2]: https://docs.sqlalchemy.org/en/13/core/type_basics.html
"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, event
from server.database import Base, db_session
from datetime import datetime
import enum

###########
## Enums ##
###########
class FeelingStatus(enum.IntEnum):
    HAPPY = 0
    SAD   = 1

############
## Models ##
############
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    feeling = Column(Enum(FeelingStatus))
    last_activity = Column(DateTime)

    def __init__(self, login):
        self.login = login
        self.feeling = FeelingStatus.HAPPY
        self.last_activity = datetime.now()

@event.listens_for(User.__table__, 'after_create')
def insert_initial_user(*args, **kwargs):
    """
        Example function that listens for the after_create event for a 
        table. In this case, it's adding an initial pre-determined value
        to the User table.
    """
    user = User("Yohlo")
    db_session.add(user)
    db_session.commit()