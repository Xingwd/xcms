from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config
from elasticsearch import Elasticsearch


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


    @app.route('/')
    def index():
        return render_template('index.html')


    from app.admin import admin
    app.register_blueprint(admin.bp)

    from app.errors import handlers
    app.register_blueprint(handlers.bp)

    from app.blog import blog
    app.register_blueprint(blog.bp)

    from app.auth import auth
    app.register_blueprint(auth.bp)

    from app.tag import tag
    app.register_blueprint(tag.bp)

    from app.proj import proj
    app.register_blueprint(proj.bp)

    from app.xuesi import xuesi
    app.register_blueprint(xuesi.bp)

    from app.info import info
    app.register_blueprint(info.bp)

    return app


# 解决循环导入问题
from app.models import User