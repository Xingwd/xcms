from flask import Blueprint, request, jsonify, abort, current_app
from main.mongodb_dm import Blog
from main.auth import auth


bp = Blueprint('blog', __name__)


@bp.route('', methods=['GET'])
def get_blogs():
    page = request.args.get('page', 1)
    limit = request.args.get('limit', current_app.config['BLOG_LIMIT'])
    docs = [doc for doc in Blog().blogs(page, limit)]
    return jsonify(docs)


@bp.route('/<int:id>', methods=['GET'])
def get_blog(id):
    blog = Blog().blog(id)
    if blog:
        return jsonify(blog)
    else:
        abort(404)


@bp.route('', methods=['POST'])
@auth.login_required
def post_blog():
    if not request.json:
        abort(400)
    if 'title' not in request.json or 'author' not in request.json:
        abort(400)
    title = request.json.get('title')
    author = request.json.get('author')
    tags = request.json.get('tags')
    content = request.json.get('content')
    publish_time = request.json.get('publish_time')

    if isinstance(tags, list):
        tags = list(set(tags))

    if Blog().insert_one(title, author, tags, content, publish_time=publish_time):
        current_app.logger.info('Created a blog')
        return jsonify({'message': 'Created'}), 201
    else:
        return jsonify({'message': 'Title <{}> is existed'.format(title)}), 409


@bp.route('/<int:id>', methods=['PUT'])
@auth.login_required
def put_blog(id):
    if not request.json:
        abort(400)
    if 'title' not in request.json or 'author' not in request.json:
        abort(400)
    title = request.json.get('title')
    author = request.json.get('author')
    tags = request.json.get('tags')
    content = request.json.get('content')

    if isinstance(tags, list):
        tags = list(set(tags))

    if Blog().update_one(id, title, author, tags, content):
        current_app.logger.info('Updated a blog')
        return jsonify({'message': 'Updated'}), 201
    else:
        return jsonify({'message': 'Id <{}> is not existed'.format(id)}), 404


@bp.route('/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_blog(id):
    Blog().delete_one(id)
    current_app.logger.info('Deleted a blog')
    return jsonify({'message': 'Deleted'}), 201
