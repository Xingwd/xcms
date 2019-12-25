from flask import Blueprint
from main.auth import auth


bp = Blueprint('blog', __name__)

# TODO: 开发增删改查逻辑
@bp.route('', methods=['GET'])
def get_blogs():
    pass


@bp.route('/<int:id>', methods=['GET'])
def get_blog(id):
    pass


@bp.route('', methods=['POST'])
@auth.login_required
def post_blog():
    pass


@bp.route('/<int:id>', methods=['PUT'])
@auth.login_required
def put_blog(id):
    pass


@bp.route('/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_blog(id):
    pass


# TODO: 开发tag相关的接口
