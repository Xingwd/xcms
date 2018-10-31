from flask import (
    Blueprint, render_template, flash, redirect, url_for
)
from flask_login import login_required

from app import db
from app.admin.forms import NewPostForm, NewTagForm
from app.models import Tag, Post


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
#@login_required
def admin():
    return render_template('admin/admin.html')

@bp.route('/admin_blog')
#@login_required
def admin_blog():
    return render_template('admin/admin_blog.html')

@bp.route('/admin_reading')
@login_required
def admin_reading():
    return render_template('admin/admin_reading.html')

@bp.route('/admin_travel')
@login_required
def admin_travel():
    return render_template('admin/admin_travel.html')

@bp.route('/admin_photography')
@login_required
def admin_photography():
    return render_template('admin/admin_photography.html')

@bp.route('/new_blog')
#@login_required
def admin_new_blog():
    post_form = NewPostForm()
    post_form.tags.choices = [(tag.name, tag.name) for tag in Tag.query.all()]
    tag_form = NewTagForm()
    if post_form.validate_on_submit():
        post = Post(title=post_form.title.data, slug=post_form.slug.data, tags=post_form.tags.data)
        db.session.add(post)
        db.session.commit()
        flash('新文章发布成功!')
        return redirect(url_for('admin.blog'))

    return render_template('admin/admin_new_blog.html', post_form=post_form, tag_form=tag_form)

@bp.route('/new_blog_tag')
def new_blog_tag():
    tag_form = NewTagForm()
    if tag_form.validate_on_submit():
        tag = Tag(name=tag_form.name.data)
        db.session.add(tag)
        db.session.commit()
        flash('新标签创建成功!')



@bp.route('/new_reading')
@login_required
def admin_new_reading():
    return render_template('admin/admin_new_reading.html')

@bp.route('/new_travel')
@login_required
def admin_new_travel():
    return render_template('admin/admin_new_travel.html')

@bp.route('/new_photography')
@login_required
def admin_new_photography():
    return render_template('admin/admin_new_photography.html')