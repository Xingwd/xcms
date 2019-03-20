from flask import (
    Blueprint, render_template, request, current_app, url_for
)
from app.models import Post, Tag
from app.blog.blog import count


bp = Blueprint('tag', __name__, url_prefix='/tag')


@bp.route('/')
def tag():
    tags = Tag.query.all()
    return render_template('tag/tag.html', tags=tags)


@bp.route('/<name>')
def tag_filter(name):
    page = request.args.get('page', 1, type=int)
    posts = Tag.query.filter_by(name=name).first_or_404().posts.order_by(Post.pub_date.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('tag.tag_filter', name=name, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('tag.tag_filter', name=name, page=posts.prev_num) \
        if posts.has_prev else None

    post_count, pv_count = count()

    return render_template('tag/tag_filter.html', posts=posts.items, next_url=next_url,
                           prev_url=prev_url, post_count=post_count, pv_count=pv_count)