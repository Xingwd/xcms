from flask import (
    Blueprint, render_template
)
from flask_login import login_required


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
@login_required
def admin():
    return render_template('admin/admin.html')

@bp.route('/admin_blog')
@login_required
def admin_blog():
    return render_template('admin/admin_blog.html')


@bp.route('/new_blog')
@login_required
def admin_new_blog():
    return render_template('admin/admin_new_blog.html')