from flask import (
    Blueprint, render_template
)



bp = Blueprint('photography', __name__, url_prefix='/photography')


@bp.route('/')
def photography():
    return render_template('photography/photography.html')



