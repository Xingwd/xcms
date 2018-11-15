from flask import (
    Blueprint, render_template, request, current_app, url_for, g, redirect
)
from app import db
from app.models import Post, Tag
from app.forms import SearchForm
from sqlalchemy import or_


bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.before_app_request
def before_request():
    g.search_form = SearchForm()


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
    post_all = Post.query.all()
    pv_count = 0
    for post in post_all:
        pv_count += post.pv

    return render_template('blog/blog.html', posts=posts.items, next_url=next_url,
                           prev_url=prev_url, tags=tags, post_all=post_all, pv_count=pv_count)

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

    # 每次访问都更新PV
    current_post.pv += 1
    db.session.commit()

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


@bp.route('/search')
def search():
    if not g.search_form.validate():
        return redirect(url_for('blog.blog'))
    page = request.args.get('page', 1, type=int)
    tags = Tag.query.all()

    if current_app.elasticsearch:
        posts, total = Post.search(g.search_form.q.data, page,
                                   current_app.config['POSTS_PER_PAGE'])
        next_url = url_for('blog.search', q=g.search_form.q.data, page=page + 1) \
            if total > page * current_app.config['POSTS_PER_PAGE'] else None
        prev_url = url_for('blog.search', q=g.search_form.q.data, page=page - 1) \
            if page > 1 else None

        return render_template('blog/search.html', posts=posts, next_url=next_url,
                               prev_url=prev_url, tags=tags)

    else:
        posts = Post.query.filter(or_(Post.title.contains(g.search_form.q.data),
                                             Post.content.contains(g.search_form.q.data))).order_by(
                                             Post.pub_date.desc()).paginate(
                                             page, current_app.config['POSTS_PER_PAGE'], False)

        next_url = url_for('blog.search', q=g.search_form.q.data, page=posts.next_num) \
            if posts.has_next else None
        prev_url = url_for('blog.search', q=g.search_form.q.data, page=posts.prev_num) \
            if posts.has_prev else None

        return render_template('blog/search.html', posts=posts.items, next_url=next_url,
                               prev_url=prev_url, tags=tags)