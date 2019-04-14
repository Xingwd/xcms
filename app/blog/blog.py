from flask import (
    Blueprint, render_template, request, current_app, url_for, g, redirect
)
from app import db
from app.models import Post
from app.forms import SearchForm
from sqlalchemy import or_


bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.before_app_request
def before_request():
    g.search_form = SearchForm()


def count():
    post_all = Post.query.all()
    post_count = len(post_all)
    pv_count = 0
    for post in post_all:
        pv_count += post.pv

    return post_count, pv_count


@bp.route('/', methods=['GET', 'POST'])
def blog():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.id.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)

    post_count, pv_count = count()

    return render_template('blog/blog.html', pagination=pagination,
                           post_count=post_count, pv_count=pv_count)


@bp.route('/detail/<slug>')
def detail(slug):
    current_post = Post.query.filter_by(slug=slug).first_or_404()

    # 每次访问都更新PV
    current_post.pv += 1
    db.session.commit()

    # 使用分页确定对象的前后关联，一个对象分为一页
    # 倒排，对象的倒排位置，即是其所在分页页码
    current_page = Post.query.filter(Post.id >= current_post.id).count()
    pages = Post.query.order_by(Post.id.desc()).paginate(
        current_page, 1, False)

    # 上一个对象
    prev_post = pages.prev().items[0] if pages.has_prev else None
    # 下一个对象
    next_post = pages.next().items[0] if pages.has_next else None

    return render_template('blog/detail.html', post=current_post,
                           prev_post=prev_post, next_post=next_post)


@bp.route('/search')
def search():
    if not g.search_form.validate():
        return redirect(url_for('blog.blog'))
    page = request.args.get('page', 1, type=int)
    post_count, pv_count = count()

    if current_app.elasticsearch:
        posts, total = Post.search(g.search_form.q.data, page,
                                   current_app.config['POSTS_PER_PAGE'])
        next_url = url_for('blog.search', q=g.search_form.q.data, page=page + 1) \
            if total > page * current_app.config['POSTS_PER_PAGE'] else None
        prev_url = url_for('blog.search', q=g.search_form.q.data, page=page - 1) \
            if page > 1 else None

        return render_template('blog/search.html', posts=posts, next_url=next_url,
                               prev_url=prev_url, post_count=post_count, pv_count=pv_count)

    else:
        posts = Post.query.filter(
            or_(Post.title.ilike("%{}%".format(g.search_form.q.data)),
                Post.content.ilike("%{}%".format(g.search_form.q.data)))).order_by(
            Post.pub_date.desc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False)

        next_url = url_for('blog.search', q=g.search_form.q.data, page=posts.next_num) \
            if posts.has_next else None
        prev_url = url_for('blog.search', q=g.search_form.q.data, page=posts.prev_num) \
            if posts.has_prev else None

        return render_template('blog/search.html', posts=posts.items, next_url=next_url,
                               prev_url=prev_url, post_count=post_count, pv_count=pv_count)