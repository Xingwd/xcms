from flask import (
    Blueprint, render_template, request, current_app, url_for
)
from app.models import Post, Tag


bp = Blueprint('blog', __name__, url_prefix='/blog')


@bp.route('/', methods=['GET', 'POST'])
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.pub_date.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('blog.blog', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('blog.blog', page=posts.prev_num) \
        if posts.has_prev else None

    tags = Tag.query.all()
    return render_template('blog/blog.html', posts=posts.items, next_url=next_url,
                           prev_url=prev_url, tags=tags)

@bp.route('/detail')
def detail():
    return render_template('blog/detail.html')


