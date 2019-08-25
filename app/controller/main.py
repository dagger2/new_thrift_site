from flask import (
    Blueprint, render_template, app, Flask
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html',
                           title='Cornell Thrift Test')

@bp.route('/hello')
def hello():
    return render_template('main/hello.html')