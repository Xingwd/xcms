# -*- coding: UTF-8 -*-
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from logging.config import dictConfig
from conf.config import DevelopmentConfig


def create_app(config=DevelopmentConfig):

    # logging 配置，在创建应用对象之前进行配置
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

    app = Flask(__name__)  # 创建应用对象
    CORS(app)  # 解决ajax跨域问题
    app.config.from_object(config)
    app.db = MongoClient(config.MONGO_HOST, config.MONGO_PORT)[config.MONGO_DB]  # mongo数据库实例

    # 测试接口
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Blueprint
    from main.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    from main.blog import bp as blog_bp
    app.register_blueprint(blog_bp, url_prefix='/api/blogs')

    return app
