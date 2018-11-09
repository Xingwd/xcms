import unittest
from app import create_app, db
from app.models import Post, Tag
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None


class TagModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_tag_posts(self):
        t = Tag(name='X')

        p1 = Post(title='X Blog', slug='x_blog', outline='xing', content='xing')
        p2 = Post(title='W Blog', slug='w_blog', outline='wei', content='wei')
        p3 = Post(title='D Blog', slug='d_blog', outline='dong', content='dong')

        p1.add_tag(t)
        p2.add_tag(t)
        p3.add_tag(t)

        db.session.add_all([t, p1, p2, p3])
        db.session.commit()

        t1 = Tag.query.filter_by(name='X').first_or_404()

        t_posts = t1.posts.all()
        self.assertEqual(len(t_posts), 3)

        p = Post.query.filter_by(title='D Blog').first_or_404()
        p.remove_tag(t1)
        t1_posts = t1.posts.all()
        self.assertEqual(len(t1_posts), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)