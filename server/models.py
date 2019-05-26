from werkzeug.security import generate_password_hash, check_password_hash


class User():
    """User Model"""

    tablename = 'user'

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def model(self):
        """Define a model"""
        model = {
            'username': self.username,
            'email': self.email,
            'password': self.hash_password()
        }
        return model

    def hash_password(self):
        """Hash a password"""
        return generate_password_hash(self.password)

    def check_password(self, password):
        """Check a password"""
        return check_password_hash(self.hash_password(), password)
