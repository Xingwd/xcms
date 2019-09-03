from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from server.models import User


bp = Blueprint('auth', __name__)

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = User(username)
    if user.user:
        return user.check_password(password)
    return False


@bp.route('/register', methods=['POST'])
def register():  # TODO: 注册模块
    pass
