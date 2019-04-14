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
    pagination = Tag.query.filter_by(name=name).first_or_404().posts.order_by(Post.id.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)

    post_count, pv_count = count()

    return render_template('tag/tag_filter.html', pagination=pagination,
                           post_count=post_count, pv_count=pv_count)