from flask import (
    Blueprint, render_template
)



bp = Blueprint('blog', __name__, url_prefix='/blog')


@bp.route('/')
def blog():
    return render_template('blog/blog.html')

@bp.route('/detail')
def detail():
    return render_template('blog/detail.html')


