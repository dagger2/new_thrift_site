from flask import (
    Blueprint, render_template, app, Flask
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html',
                           title='Cornell Thrift')

@bp.route('/events/ezras_exchange')
def ezras_exchange():
    return render_template('main/hello.html')

@bp.route('/events/mending-workshops')
def mending_workshops():
    return render_template('main/hello.html')

@bp.route('/members')
def members():
    return render_template('main/members.html')

@bp.route('/contact')
def contact():
    return render_template('main/contact.html')

@bp.route('/events')
def events():
    return render_template('main/events.html')

@bp.route('/events/pop-up-shops')
def pop_up_shops():
    return render_template('main/hello.html')

@bp.route('/hello')
def hello():
    return render_template('main/hello.html')

@bp.route('/dino-game')
def dino_game():
    return render_template('main/dino_game.html')

# @bp.errorhandler(404)
