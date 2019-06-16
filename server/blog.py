from flask import Blueprint, request, jsonify
from server.models import Blog
from server.auth import auth


bp = Blueprint('blog', __name__)


@bp.route('/', methods=['GET'])
def get_blogs():
    page = request.args.get('page', 1)
    limit = request.args.get('limit', 3)
    blogs = []
    docs = Blog.blogs(page, limit)
    if len(docs) > 0:
        for i in docs:
            del i['_id']
            blogs.append(i)
    return jsonify(blogs)


@bp.route('/<string:slug>', methods=['GET'])
def get_blog(slug):
    blog = Blog(slug).blog
    if blog:
        del blog['_id']
        return jsonify(blog)
    else:
        return None


@bp.route('/', methods=['POST'])
@auth.login_required
def post_blog():  # TODO: 新建博客的逻辑
    pass


@bp.route('/<string:slug>', methods=['PUT'])
@auth.login_required
def put_blog():  # TODO: 编辑博客的逻辑
    pass


@bp.route('/<string:slug>', methods=['DELETE'])
@auth.login_required
def delete_blog():  # TODO: 删除博客的逻辑
    pass
