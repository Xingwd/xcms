import time
from flask import (
    Blueprint, render_template, redirect, url_for, jsonify, request, g
)
from flask_login import login_required
from sqlalchemy import or_

from app import db
from app.admin.forms import NewPostForm, NewTagForm, AdminSearchForm
from app.models import Tag, Post


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.before_app_request
def before_request():
    g.admin_search_form = AdminSearchForm()


@bp.route('/')
@login_required
def admin():
    return render_template('admin/admin.html')

@bp.route('/admin_blog')
@login_required
def admin_blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.pub_date.desc()).paginate(
        page, 10, False)
    next_url = url_for('admin.admin_blog', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('admin.admin_blog', page=posts.prev_num) \
        if posts.has_prev else None

    return render_template('admin/blog/admin_blog.html', admin_search_form=g.admin_search_form,
                           posts=posts.items, next_url=next_url, prev_url=prev_url)

@bp.route('/search_blog')
@login_required
def search_blog():
    if not g.admin_search_form.validate():
        return redirect(url_for('admin.admin_blog'))

    page = request.args.get('page', 1, type=int)

    posts = Post.query.filter(
        or_(Post.title.ilike("%{}%".format(g.admin_search_form.q.data)),
            Post.content.ilike("%{}%".format(g.admin_search_form.q.data)))).order_by(
        Post.pub_date.desc()).paginate(
        page, 10, False)

    next_url = url_for('admin.search_blog', q=g.admin_search_form.q.data, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('admin.search_blog', q=g.admin_search_form.q.data, page=posts.prev_num) \
        if posts.has_prev else None

    return render_template('admin/blog/search_blog.html', posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


@bp.route('/admin_blog_tag')
@login_required
def admin_blog_tag():
    tags = Tag.query.order_by(Tag.id.desc()).all()
    return render_template('admin/blog/admin_blog_tag.html', tags=tags)

@bp.route('/new_blog', methods=['GET', 'POST'])
@login_required
def new_blog():
    g.post_id = None
    post_form = NewPostForm()
    post_form.tags.choices = [(tag.name, tag.name) for tag in Tag.query.all()]
    if post_form.validate_on_submit():
        post = Post(title=post_form.title.data, slug=post_form.slug.data,
                    outline=post_form.outline.data,
                    content=post_form.content.data,
                    pub_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        for tag in post_form.tags.data:
            post.add_tag(Tag.query.filter_by(name=tag).first())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('admin.admin_blog'))

    return render_template('admin/blog/edit_blog.html', post_form=post_form)

@bp.route('/new_blog_tag', methods=['GET', 'POST'])
@login_required
def new_blog_tag():
    new_tag = request.form.get('tag_name')
    if Tag.query.filter_by(name=new_tag).first() is not None:
        return jsonify(newtag=new_tag, b=True)
    else:
        tag = Tag(name=new_tag)
        db.session.add(tag)
        db.session.commit()
        return jsonify(newtag=new_tag, b=False)


@bp.route('/edit_blog/<id>', methods=['GET', 'POST'])
@login_required
def edit_blog(id):
    g.post_id = id
    post = Post.query.filter_by(id=id).first_or_404()
    tags = [tag.name for tag in post.tags]

    post_form = NewPostForm()
    post_form.tags.choices = [(tag.name, tag.name) for tag in Tag.query.all()]
    post_form.tags.data = tags
    post_form.outline.data = post.outline
    post_form.content.data = post.content

    tag_form = NewTagForm()

    if post_form.validate_on_submit():
        post.title = post_form.title.data
        post.slug = post_form.slug.data
        post.outline = request.form.get('outline')
        post.content = request.form.get('content')
        new_tags = request.form.getlist('tags')

        add_list = list(set(new_tags).difference(set(tags)))
        remove_list = list(set(tags).difference(set(new_tags)))
        if new_tags != tags:
            if len(add_list):
                for tag in add_list:
                    post.add_tag(Tag.query.filter_by(name=tag).first())
            if len(remove_list):
                for tag in remove_list:
                    post.remove_tag(Tag.query.filter_by(name=tag).first())

        db.session.commit()
        return redirect(url_for('admin.admin_blog'))

    return render_template('admin/blog/edit_blog.html',
                           post_form=post_form, tag_form=tag_form, post=post)


@bp.route('/edit_blog_tag/<id>', methods=['GET', 'POST'])
@login_required
def edit_blog_tag(id):
    g.tag_id = id
    tag = Tag.query.filter_by(id=id).first_or_404()
    tag_form = NewTagForm()
    if tag_form.validate_on_submit():
        tag.name = tag_form.tag_name.data
        db.session.commit()
        return redirect(url_for('admin.admin_blog_tag'))

    return render_template('admin/blog/edit_blog_tag.html', tag=tag, tag_form=tag_form)


@bp.route('/del_blog/<id>', methods=['GET', 'POST'])
@login_required
def del_blog(id):
    post = Post.query.filter_by(id=id).first_or_404()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('admin.admin_blog'))

@bp.route('/del_blog_tag/<id>', methods=['GET', 'POST'])
@login_required
def del_blog_tag(id):
    tag = Tag.query.filter_by(id=id).first_or_404()
    db.session.delete(tag)
    db.session.commit()
    return redirect(url_for('admin.admin_blog_tag'))



@bp.route('/admin_reading')
@login_required
def admin_reading():
    return render_template('admin/reading/admin_reading.html')

@bp.route('/new_reading', methods=['GET', 'POST'])
@login_required
def new_reading():
    return render_template('admin/reading/new_reading.html')

@bp.route('/admin_travel')
@login_required
def admin_travel():
    return render_template('admin/travel/admin_travel.html')

@bp.route('/new_travel', methods=['GET', 'POST'])
@login_required
def new_travel():
    return render_template('admin/travel/new_travel.html')

@bp.route('/admin_photography')
@login_required
def admin_photography():
    return render_template('admin/photography/admin_photography.html')

@bp.route('/new_photography', methods=['GET', 'POST'])
@login_required
def new_photography():
    return render_template('admin/photography/new_photography.html')