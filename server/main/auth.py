from flask import Blueprint, request, abort, current_app, jsonify
from flask_httpauth import HTTPBasicAuth
from server.main.mongodb_dm import User


bp = Blueprint('auth', __name__)

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = User()
    if user.user(username):
        return user.check_password(username, password)
    return False


@bp.route('/register', methods=['POST'])
def register():
    if not request.json:
        abort(400)
    if 'username' not in request.json or 'password' not in request.json:
        abort(400)
    username = request.json.get('username')
    password = request.json.get('password')

    if User().insert_one(username, password):
        current_app.logger.info('Created a user')
        return jsonify({'message': 'Created'}), 201
    else:
        return jsonify({'message': 'Username <{}> is existed'.format(username)}), 409
