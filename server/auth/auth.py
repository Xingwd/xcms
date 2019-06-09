from flask import Blueprint, request, jsonify, current_app
from flask_login import login_user, login_required, logout_user
from server.models import User


bp = Blueprint('auth', __name__)


@bp.route('/login', methods=('POST'))
def login():
    if 'username' not in request.json or 'password' not in request.json:
        return jsonify({'status': 'error', 'message': 'Username and password is required.'})
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username is None or password is None:
        return jsonify({'status': 'error', 'message': 'Username and password can\'t be null.'})
    user = current_app.db[User.tablename].find_one({'username': username})
    if user is None:
        return jsonify({'status': 'error', 'message': 'User is not existed.'})
    if not User.check_password(user.password_hash, password):
        return jsonify({'status': 'error', 'message': 'Password is wrong.'})
    login_user(user, remember=request.json.get('remember_me'))
    return jsonify({'status': 'success', 'message': 'Login successfully.'})


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'status': 'success', 'message': 'Logout successfully.'})


@bp.route('/register', methods=('POST'))
def register():
    if 'username' not in request.json or 'password' not in request.json:
        return jsonify({'status': 'error', 'message': 'Username and password is required.'})
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username is None or password is None:
        return jsonify({'status': 'error', 'message': 'Username and password can\'t be null.'})
    if current_app.db[User.tablename].find_one({'username': username}):
        return jsonify({'status': 'error', 'message': 'Username is existed.'})
    current_app.db[User.tablename].insert_one({'username': username, 'password_hash': User.hash_password(password)})
    return jsonify({'status': 'success', 'message': 'Registered successfully.'})
