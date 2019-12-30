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
    category_name = request.args.get('category_name')
    pagination = None
    data = {}
    if category_name:
        category = Category.query.filter_by(name=category_name).first_or_404()
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
                'body': i.body,
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
        'body': post.body,
        'category_id': post.category_id,
        'category': post.category.name if post.category_id else None
    }
    return jsonify(data)


@bp.route('/v1.0/posts', methods=['POST'])
@auth.login_required
def create_post():
    if not request.json or 'title' not in request.json or 'category_name' not in request.json:
        abort(400)
    category = Category.query.filter_by(name=request.json['category_name']).first()
    if not category:
        return jsonify({'msg': 'Category <{}> does not exist', 'status_code': 404}), 404
    post = Post(title=request.json['title'], body=request.json.get('body', ''), category_id=category.id)
    db.session.add(post)
    db.session.commit()
    return jsonify({'msg': 'Created the blog', 'status_code': 201}), 201


@bp.route('/v1.0/posts/<int:id>', methods=['PUT'])
@auth.login_required
def update_post(id):
    if not request.json or 'title' not in request.json:
        abort(400)
    post = Post.query.filter_by(id=id).first_or_404()
    post.title = request.json['title']
    post.body = request.json.get('body', '')
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
        data.append({
            'id': category.id,
            'name': category.name
        })
    return jsonify(data)


@bp.route('/v1.0/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.filter_by(id=id).first_or_404()
    data = {
        'id': category.id,
        'name': category.name
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
