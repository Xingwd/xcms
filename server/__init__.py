# -*- coding: UTF-8 -*-
from conf.config import ProductionConfig, DevelopmentConfig
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient


def create_app(config=ProductionConfig):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    # mongo数据库实例
    app.db = MongoClient(config.MONGO_HOST, config.MONGO_PORT)[config.XCMS_DB]

    # Blueprint
    from auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from blog import bp as blog_bp
    app.register_blueprint(blog_bp, url_prefix='/blogs')

    return app


if __name__ == '__main__':
    app = create_app(config=DevelopmentConfig)
    app.run(host='0.0.0.0')
