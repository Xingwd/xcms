from flask import (
    Blueprint, render_template
)



bp = Blueprint('proj', __name__, url_prefix='/proj')


@bp.route('/')
def proj():
    return render_template('proj/proj.html')



