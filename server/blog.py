from flask import Blueprint, request, jsonify, abort
from server.models import Blog
from server.auth import auth


bp = Blueprint('blog', __name__)


@bp.route('/', methods=['GET'])
def get_blogs():
    page = request.args.get('page', 1)
    limit = request.args.get('limit', 3)
    blogs = []
    docs = Blog.blogs(page, limit)
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
        abort(404)


@bp.route('/', methods=['POST'])
@auth.login_required
def post_blog():
    if not request.json:
        abort(400)
    if 'title' not in request.json or 'slug' not in request.json:
        abort(400)
    title = request.json.get('title')
    slug = request.json.get('slug')
    tag = request.json.get('tag')
    content = request.json.get('content')

    if isinstance(tag, list):
        tag = list(set(tag))

    Blog.new_blog(title, slug, tag, content)
    return jsonify({'message': 'Created'}), 201


@bp.route('/<string:slug>', methods=['PUT'])
@auth.login_required
def put_blog(slug):
    if not request.json:
        abort(400)
    if 'title' not in request.json or 'slug' not in request.json:
        abort(400)
    title = request.json.get('title')
    slug = request.json.get('slug')
    tag = request.json.get('tag')
    content = request.json.get('content')

    if isinstance(tag, list):
        tag = list(set(tag))

    Blog(slug).update_blog(title, slug, tag, content)
    return jsonify({'message': 'Updated'}), 201


@bp.route('/<string:slug>', methods=['DELETE'])
@auth.login_required
def delete_blog(slug):
    Blog(slug).delete_blog()
    return jsonify({'message': 'Deleted'}), 201
