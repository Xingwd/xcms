from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class BlogPost(db.Model):
    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, index=True)
    body = db.Column(db.Text, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('blog_category.id'), index=True)
    category = db.relationship('BlogCategory', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title


class BlogCategory(db.Model):
    __tablename__ = 'blog_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, index=True)

    def __repr__(self):
        return '<Category %r>' % self.name
