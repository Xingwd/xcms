# -*- coding: UTF-8 -*-
from flask import Blueprint, request, jsonify, abort
from . import db
from .models import History
from .auth import auth


bp = Blueprint('history', __name__)


@bp.route('/v1.0/histories', methods=['GET'])
def get_histories():
    data = []
    for h in History.query.order_by(History.id.desc()).all():
        data.append({
            'time': h.time,
            'release': h.release,
            'description': h.description
        })
    return jsonify(data)


@bp.route('/v1.0/histories', methods=['POST'])
@auth.login_required
def create_history():
    if not request.json or 'time' not in request.json:
        abort(400)
    if 'release' not in request.json or 'description' not in request.json:
        abort(400)
    history = History(time=request.json['time'],
                      release=request.json['release'],
                      description=request.json['description'])
    db.session.add(history)
    db.session.commit()
    return jsonify({'msg': 'Created the history', 'status_code': 201}), 201


@bp.route('/v1.0/histories/<int:id>', methods=['PUT'])
@auth.login_required
def update_history(id):
    if not request.json or 'time' not in request.json:
        abort(400)
    if 'release' not in request.json or 'description' not in request.json:
        abort(400)
    history = History.query.filter_by(id=id).first_or_404()
    history.time = request.json['time']
    history.release = request.json['release']
    history.description = request.json['description']
    db.session.commit()
    return jsonify({'msg': 'Updated the history', 'status_code': 201}), 201


@bp.route('/v1.0/histories/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_history(id):
    history = History.query.filter_by(id=id).first_or_404()
    db.session.delete(history)
    db.session.commit()
    return jsonify({'msg': 'Deleted the history', 'status_code': 201}), 201
