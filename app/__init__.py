from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config


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


    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about_me():
        return render_template('about_me.html')

    from app.admin import admin
    app.register_blueprint(admin.bp)

    from app.blog import blog
    app.register_blueprint(blog.bp)

    from app.auth import auth
    app.register_blueprint(auth.bp)

    from app.reading import reading
    app.register_blueprint(reading.bp)

    from app.travel import travel
    app.register_blueprint(travel.bp)

    from app.photography import photography
    app.register_blueprint(photography.bp)

    return app


# 解决循环导入问题
from app.models import User