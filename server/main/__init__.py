# -*- coding: UTF-8 -*-
from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from logging.config import dictConfig
from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=DevelopmentConfig):

    # https://dormousehole.readthedocs.io/en/latest/logging.html#logging
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

    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.errorhandler
    # https://dormousehole.readthedocs.io/en/latest/errorhandling.html#error-handlers
    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'msg': 'Not found', 'status_code': 404}), 404)

    @app.errorhandler(400)
    def bad_request(error):
        return make_response(jsonify({'msg': 'Bad request', 'status_code': 400}), 400)

    # 测试接口
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Blueprint
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/xcms/auth/api')
    # TODO: 更新url_prefix=/api/<module>
    from .blog import bp as blog_bp
    app.register_blueprint(blog_bp, url_prefix='/xcms/blog/api')

    return app
