from flask import (
    Blueprint, render_template
)
from app.models import Tag


bp = Blueprint('xuesi', __name__, url_prefix='/xuesi')


@bp.route('/')
def xuesi():
    tags = Tag.query.all()
    return render_template('xuesi/xuesi.html', tags=tags)



