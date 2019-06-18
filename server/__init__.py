# -*- coding: UTF-8 -*-
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient


def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    # mongo数据库实例
    app.db = MongoClient(config.MONGO_HOST, config.MONGO_PORT)[config.MONGO_DB]

    # Blueprint
    from server.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/xcms/api/auth')

    from server.blog import bp as blog_bp
    app.register_blueprint(blog_bp, url_prefix='/xcms/api/blogs')

    return app
