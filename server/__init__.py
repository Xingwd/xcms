# -*- coding: UTF-8 -*-
from conf.config import ProductionConfig, DevelopmentConfig
from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient
from models import User


login_manager = LoginManager()


def create_app(config=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    # mongo数据库实例
    db = MongoClient(config.MONGO_HOST, config.MONGO_PORT)[config.XCMS_DB]

    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(username):  # login_manager 回调函数
        doc = db[User.tablename].find_one({'username': username})
        if doc:
            return doc
        else:
            return None

    from server.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app


if __name__ == '__main__':
    app = create_app(config=DevelopmentConfig)
    app.run(host='0.0.0.0')