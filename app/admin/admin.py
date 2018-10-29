from flask import (
    Blueprint, render_template
)


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def admin():
    return render_template('admin/admin.html')

@bp.route('/admin_blog')
def admin_blog():
    return render_template('admin/admin_blog.html')
