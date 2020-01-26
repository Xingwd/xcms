# -*- coding: UTF-8 -*-
from flask import Blueprint, request, jsonify, abort
from . import db
from .models import BlogPost as Post, BlogCategory as Category
from .auth import auth

bp = Blueprint('blog', __name__)


@bp.route('/v1.0/posts', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('page', 5, type=int)
    category_id = request.args.get('category_id')
    pagination = None
    data = {}
    if category_id:
        category = Category.query.filter_by(id=category_id).first_or_404()
        pagination = Post.query.with_parent(category).order_by(
            Post.id.desc()).paginate(page=page, per_page=limit, error_out=False)
    else:
        pagination = Post.query.order_by(Post.id.desc()).paginate(
            page=page, per_page=limit, error_out=False)
    if pagination:
        # 对象属性：https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.Pagination
        data['has_next'] = pagination.has_next
        data['has_prev'] = pagination.has_prev

        posts = []
        for i in pagination.items:
            category_name = i.category.name if i.category_id else None
            posts.append({
                'id': i.id,
                'title': i.title,
                'content': i.content,
                'category_id': i.category_id,
                'category': category_name
            })
        data['posts'] = posts
    return jsonify(data)


@bp.route('/v1.0/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'category_id': post.category_id,
        'category': post.category.name if post.category_id else None
    }
    return jsonify(data)


@bp.route('/v1.0/posts', methods=['POST'])
@auth.login_required
def create_post():
    if not request.json or 'title' not in request.json or 'category_id' not in request.json:
        abort(400)
    category = Category.query.filter_by(id=request.json['category_id']).first()
    if not category:
        return jsonify({
            'msg': 'Category <{}> does not exist'.format(request.json['category_id']),
            'status_code': 404}), 404
    post = Post(title=request.json['title'], content=request.json.get('content', ''), category_id=category.id)
    db.session.add(post)
    db.session.commit()
    return jsonify({'msg': 'Created the blog', 'status_code': 201}), 201


@bp.route('/v1.0/posts/<int:id>', methods=['PUT'])
@auth.login_required
def update_post(id):
    if not request.json or 'title' not in request.json or 'category_id' not in request.json:
        abort(400)
    category = Category.query.filter_by(id=request.json['category_id']).first()
    if not category:
        return jsonify({
            'msg': 'Category <{}> does not exist'.format(request.json['category_id']),
            'status_code': 404}), 404
    post = Post.query.filter_by(id=id).first_or_404()
    post.title = request.json['title']
    post.content = request.json.get('content', '')
    post.category_id = request.json['category_id']
    db.session.commit()
    return jsonify({'msg': 'Updated the blog', 'status_code': 201}), 201


@bp.route('/v1.0/posts/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    db.session.delete(post)
    db.session.commit()
    return jsonify({'msg': 'Deleted the blog', 'status_code': 201}), 201


@bp.route('/v1.0/categories', methods=['GET'])
def get_categories():
    data = []
    for category in Category.query.all():
        posts = []
        for post in category.posts:
            posts.append({
                'id': post.id,
                'title': post.title,
                'content': post.content
            })
        data.append({
            'id': category.id,
            'name': category.name,
            'posts': posts
        })
    return jsonify(data)


@bp.route('/v1.0/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.filter_by(id=id).first_or_404()
    posts = []
    for post in category.posts:
        posts.append({
            'id': post.id,
            'title': post.title,
            'content': post.content
        })
    data = {
        'id': category.id,
        'name': category.name,
        'posts': posts
    }
    return jsonify(data)


@bp.route('/v1.0/categories', methods=['POST'])
@auth.login_required
def create_category():
    if not request.json or 'name' not in request.json:
        abort(400)
    category = Category(name=request.json['name'])
    db.session.add(category)
    db.session.commit()
    return jsonify({'msg': 'Created the category', 'status_code': 201}), 201


@bp.route('/v1.0/categories/<int:id>', methods=['PUT'])
@auth.login_required
def update_category(id):
    if not request.json or 'name' not in request.json:
        abort(400)
    category = Category.query.filter_by(id=id).first_or_404()
    category.name = request.json['name']
    db.session.commit()
    return jsonify({'msg': 'Updated the category', 'status_code': 201}), 201


@bp.route('/v1.0/categories/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_category(id):
    category = Category.query.filter_by(id=id).first_or_404()
    db.session.delete(category)
    db.session.commit()
    return jsonify({'msg': 'Deleted the category', 'status_code': 201}), 201
