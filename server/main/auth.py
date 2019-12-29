from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from .models import User


bp = Blueprint('auth', __name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        return user.check_password(password)
    return False
# TODO: 开发认证逻辑
