import click
from . import db
from .models import User


def register(app):
    @app.cli.command('createadmin')
    @click.option('--name', default='admin', help='Admin account name, is admin by default')
    @click.option('--password', default='admin', help='Admin account password, is admin by defalut')
    def create_admin(name, password):
        """Create admin account"""
        user = User(username=name)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
