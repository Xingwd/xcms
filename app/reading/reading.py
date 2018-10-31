from flask import (
    Blueprint, render_template
)



bp = Blueprint('reading', __name__, url_prefix='/reading')


@bp.route('/')
def reading():
    return render_template('reading/reading.html')



