from flask import (
    Blueprint, render_template
)


bp = Blueprint('xuesi', __name__, url_prefix='/xuesi')


@bp.route('/')
def xuesi():
    return render_template('xuesi/xuesi.html')



