# -*- coding: UTF-8 -*-
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from . import db


class User(db.Model):  # TODO: email注册，验证码
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def check_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # 有效token，但是过期
        except BadSignature:
            return None  # 无效token
        user = User.query.get(data['id'])
        return user


class BlogPost(db.Model):
    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    pv = db.Column(db.Integer, index=True, default=0)
    # TODO: 增加时间，推荐时，做为指标使用

    category_id = db.Column(db.Integer, db.ForeignKey('blog_category.id'), index=True)
    category = db.relationship('BlogCategory', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title


class BlogCategory(db.Model):
    __tablename__ = 'blog_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, index=True)

    def __repr__(self):
        return '<Category %r>' % self.name


class History(db.Model):
    __tablename__ = 'project_history'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(20), nullable=False, index=True)
    release = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<History %r>' % self.name
