from flask import (
    Blueprint, render_template
)
from app.models import Post, Tag


bp = Blueprint('blog', __name__, url_prefix='/blog')


@bp.route('/')
def blog():
    posts = Post.query.all()
    tags = Tag.query.all()
    return render_template('blog/blog.html', posts=posts, tags=tags)

@bp.route('/detail')
def detail():
    return render_template('blog/detail.html')


