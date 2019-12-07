"""
    Main API logic for our app. 
"""
from server import app
from server.database import db_session
from server.apps.api import models, utils
from server.decorators import token_required
from flask import Blueprint, g, jsonify, request
from datetime import datetime

api = Blueprint('api', __name__)

## GET /user
# Gets details about user using the supplied GitHub access token.
# The @token_required decorator runs the logic for getting user
# info from github. Refer to server/decorators.py for more info.
@api.route('/user')
@token_required
def user():
    # search for the user in our db using their github 
    user = db_session.query(models.User) \
        .filter(models.User.login == g.user['login']) \
        .first()

    # if the user doesn't exist, create a new one!
    if not user:
        new_user = models.User(g.user['login'])
        db_session.add(new_user)
        db_session.commit()

        user = new_user
    
    # just for fun, keeping track of a users last activity!
    user.last_activity = datetime.now()
    
    # don't forget to save changes after making modifications to an entry in the db.
    db_session.commit()

    # return the user data
    num_happy, num_sad = utils.getCounts()
    return jsonify({
        'login': g.user['login'],
        'name': g.user['name'],
        'avatar_url': g.user['avatar_url'],
        'is_happy': user.feeling == models.FeelingStatus.HAPPY,
        'num_happy': num_happy,
        'num_sad': num_sad
    })

## POST /toggleHappiness
# Changes the current users 'feeling' value from either
# happy->sad or sad->happy! 
@api.route('/toggleHappiness', methods=['POST'])
@token_required
def toggle_happiness():
    user = db_session.query(models.User) \
        .filter(models.User.login == g.user['login']) \
        .first()
    
    # instead of creating a new user in this case, 
    # simply just 404. User creation should be handled by the /user request.
    if not user: return "User not found!", 404

    user.feeling = models.FeelingStatus.HAPPY if user.feeling == models.FeelingStatus.SAD else models.FeelingStatus.SAD
    user.last_activity = datetime.now()

    db_session.commit()

    num_happy, num_sad = utils.getCounts()
    return jsonify({
        'is_happy': user.feeling == models.FeelingStatus.HAPPY,
        'num_happy': num_happy,
        'num_sad': num_sad
    })
