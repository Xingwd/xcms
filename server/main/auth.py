from flask import Blueprint, request, abort, jsonify
from flask_httpauth import HTTPTokenAuth
from . import db
from .models import User


bp = Blueprint('auth', __name__)
auth = HTTPTokenAuth(scheme='Token')


@auth.verify_token
def verify_token(username_or_token, password):
    # 先尝试token认证
    user = User.check_token(username_or_token)
    if not user:
        # 尝试username/password认证
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.check_password(password):
            return False
    return True


@bp.route('/v1.0/register', methods=['POST'])
def register():
    if not request.json:
        abort(400)
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username=username).first():
        return jsonify({'msg': 'User <{}> is existed'.format(username), 'status_code': 400}), 400
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201


@bp.route('/v1.0/login', methods=['POST'])
def login():
    if not request.json:
        abort(400)
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    user = User.query.filter_by(username=username).first_or_404()
    if not user.check_password(password):
        return jsonify({'msg': 'Password is incorrect', 'status_code': 400}), 400
    token = user.generate_token()
    return jsonify({'token': token.decode('ascii')})
