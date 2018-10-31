from flask import (
    Blueprint, render_template
)
from flask_login import login_required
from app.admin.forms import NewBlogForm, NewTagForm


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
    blog_form = NewBlogForm()
    tag_form = NewTagForm()
    return render_template('admin/admin_new_blog.html', blog_form=blog_form, tag_form=tag_form)

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