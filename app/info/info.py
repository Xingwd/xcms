from flask import (
    Blueprint, render_template
)
from app.models import AboutMe, Copyright


bp = Blueprint('info', __name__, url_prefix='/info')


@bp.route('/about_me')
def about_me():
    info = AboutMe.query.order_by(AboutMe.id.desc()).first()
    return render_template('info/about_me.html', info=info)

@bp.route('/copyright')
def copyright():
    info = Copyright.query.order_by(Copyright.id.desc()).first()
    return render_template('info/copyright.html', info=info)
