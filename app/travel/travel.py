from flask import (
    Blueprint, render_template
)



bp = Blueprint('travel', __name__, url_prefix='/travel')


@bp.route('/')
def travel():
    return render_template('travel/travel.html')



