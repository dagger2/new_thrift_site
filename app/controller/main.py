from flask import (
    Blueprint, render_template, app, redirect, url_for, abort
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
    return redirect(url_for('main.happenings'))

@bp.route('/happenings')
def happenings():
    return render_template('main/happenings.html')

@bp.route('/events/pop-up-shops')
def pop_up_shops():
    return render_template('main/hello.html')

@bp.route('/hello')
def hello():
    return render_template('main/hello.html')

@bp.route('/dino-game')
def dino_game():
    return render_template('main/dino_game.html')

@bp.route('/credits')
def credits():
    return render_template('main/credits.html')





@bp.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errors/04.html'), 404

@bp.route("/<path:invalid_path>")
def handle_unmatchable(*args, **kwargs):
    abort(404)