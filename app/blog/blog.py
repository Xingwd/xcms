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

@bp.route('/tag/<name>')
def tag_filter(name):
    page = request.args.get('page', 1, type=int)
    posts = Tag.query.filter_by(name=name).first_or_404().posts.order_by(Post.pub_date.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('blog.tag_filter', name=name, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('blog.tag_filter', name=name, page=posts.prev_num) \
        if posts.has_prev else None

    tags = Tag.query.all()
    return render_template('blog/tag_filter.html', posts=posts.items, next_url=next_url,
                           prev_url=prev_url, tags=tags)


@bp.route('/detail/<slug>')
def detail(slug):
    current_post = Post.query.filter_by(slug=slug).first_or_404()
    current_page = Post.query.filter(Post.id >= current_post.id).count()
    posts = Post.query.order_by(Post.pub_date.desc()).paginate(
        current_page, 1, False)

    next_posts = Post.query.order_by(Post.pub_date.desc()).paginate(
        posts.next_num, 1, False) if posts.has_next else None
    prev_posts = Post.query.order_by(Post.pub_date.desc()).paginate(
        posts.prev_num, 1, False) if posts.has_prev else None

    next_url = url_for('blog.detail', slug=next_posts.items[0].slug) \
        if posts.has_next else None
    prev_url = url_for('blog.detail', slug=prev_posts.items[0].slug) \
        if posts.has_prev else None

    tags = Tag.query.all()
    return render_template('blog/detail.html', post=posts.items[0], next_url=next_url,
                           prev_url=prev_url, tags=tags)


