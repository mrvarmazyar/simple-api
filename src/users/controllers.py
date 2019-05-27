from http import HTTPStatus
from datetime import datetime, date

from bottle import request, response

from .models import User
from snippets import validate_data
from .constants import CREATE_SCHEMA_PATH, UPDATE_SCHEMA_PATH


def get_user(username):
    try:
        user = User.get(User.username == username)
    except User.does_not_exists:
        response.status = HTTPStatus.NOT_FOUND
        return

    if user.birthday_is_today:
        return {"message": "Hello, {username}! Happy birthday!".format(username=user.username)}
    return {
        "message": "Hello, {username}! Your date of birth is {days}".format(username=user.username,
                                                                            days=user.birth_date_diff_in_days)}


def create_user():
    error = validate_data(request.json, CREATE_SCHEMA_PATH)
    if error:
        response.status = HTTPStatus.BAD_REQUEST
        return error

    try:
        user = User.create(**request.json)
    except User.integrity_error:
        response.status = HTTPStatus.CONFLICT
        return {'error': 'username already exists'}

    response.status = HTTPStatus.CREATED
    return user.serialize()


def update_user(username):
    try:
        user = User.get(User.username == username)
    except User.does_not_exists:
        response.status = HTTPStatus.NOT_FOUND
        return

    error = validate_data(request.json, UPDATE_SCHEMA_PATH)
    if error:
        response.status = HTTPStatus.BAD_REQUEST
        return error

    if request.json.get('username'):
        user.username = request.json['username']

    if request.json.get('birthday'):
        if datetime.strptime(request.json['birthday'], '%Y-%m-%d').date() >= date.today():
            response.status = HTTPStatus.BAD_REQUEST
            return {'birthday': 'must be before today'}

        user.birthday = request.json['birthday']

    try:
        user.save()
    except User.integrity_error:
        response.status = HTTPStatus.CONFLICT
        return {'error': 'username already exists'}

    response.status = HTTPStatus.NO_CONTENT
    return


def delete_user(username):
    effected_rows = User.delete().where(User.username == username).execute()
    response.status = HTTPStatus.NO_CONTENT if effected_rows > 0 else HTTPStatus.NOT_FOUND
    return
