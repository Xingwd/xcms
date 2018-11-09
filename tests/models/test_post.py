import unittest
from app import create_app, db
from app.models import Post, Tag
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None


class PostModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_and_remove_tag(self):
        t1 = Tag(name='X')
        t2 = Tag(name='W')
        t3 = Tag(name='D')
        p = Post(title='X Blog', slug='x_blog', outline='xing', content='xing')
        p.add_tag(t1)
        p.add_tag(t2)
        p.add_tag(t3)
        db.session.add_all([t1, t2, t3, p])
        db.session.commit()

        self.assertEqual(len(p.tags), 3)

        t = Tag.query.filter_by(name='X').first_or_404()
        p1 = Post.query.filter_by(title='X Blog').first_or_404()
        p1.remove_tag(t)

        self.assertEqual(len(p1.tags), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)