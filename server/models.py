from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
    """User Model.

    Parameters
    ----------
    username : string
        User name.

    Attributes
    ----------
    tablename : string
        Name of user table.

    """

    tablename = 'user'

    def __init__(self, username):
        self.username = username

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        self.username

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

    @staticmethod
    def check_password(password_hash, password):
        """Check a password.

        Parameters
        ----------
        password_hash : string
            A user password_hash in db.
        password : type
            A password user typed.

        Returns
        -------
        boolen
            True of False.

        """
        return check_password_hash(password_hash, password)
