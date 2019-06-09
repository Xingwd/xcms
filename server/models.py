from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
    """User Model.

    Parameters
    ----------
    username : string
        User name.

    Attributes
    ----------
    user : object
        A user object.
    tablename : string
        Name of user table.

    """
    tablename = 'user'

    def __init__(self, username):
        self.user = current_app.db[self.tablename].find_one({'username': self.username})

    @property
    def user(self):
        return self.user

    @staticmethod
    def hash_password(password):
        """Hash a password.

        Parameters
        ----------
        password : string
            Password of a user.

        Returns
        -------
        string
            Password hash.

        """
        return generate_password_hash(password)

    def check_password(self, password):
        """Check a password.

        Parameters
        ----------
        password : type
            A password user typed.

        Returns
        -------
        boolen
            True of False.

        """
        return check_password_hash(self.user['password_hash'], password)


class Blog(object):
    tablename = 'blog'

    def __init__(self, slug):
        self.blog = current_app.db[self.tablename].find_one({'slug': slug})

    @property
    def blog(self):
        return self.blog

    @staticmethod
    def blogs(page, limit):
        return current_app.db[Blog.tablename].find().skip((page-1)*limit).limit(limit)
