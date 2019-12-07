"""
    Can keep utility logic in this file.
    Completely optional to use, but it does separate some logic out 
    from other files.
"""
from server.database import db_session
from server.apps.api import models

def getCounts():
    """
        Simply counts the number of happy and number of sad people!
    """
    num_happy = db_session.query(models.User).filter(models.User.feeling == models.FeelingStatus.HAPPY).count()
    num_sad = db_session.query(models.User).filter(models.User.feeling == models.FeelingStatus.SAD).count()

    return num_happy, num_sad