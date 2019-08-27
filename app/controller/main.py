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
    return render_template('main/happenings.html')

@bp.route('/events/mending-workshops')
def mending_workshops():
    return render_template('main/happenings.html')

@bp.route('/resources')
def resources():
    return render_template('main/resources.html')

@bp.route('/members')
def members():
    return render_template('main/members.html')

@bp.route('/connect')
def connect():
    return render_template('main/connect.html')

@bp.route('/contact')
def contact():
    return redirect(url_for('main.connect'))

@bp.route('/events')
def events():
    return redirect(url_for('main.happenings'))

@bp.route('/happenings')
def happenings():
    return render_template('main/happenings.html')

@bp.route('/events/pop-up-shops')
def pop_up_shops():
    return render_template('main/events.html')

@bp.route('/dino-game')
def dino_game():
    return render_template('main/dino_game.html')

@bp.route('/credits')
def credits():
    return render_template('main/credits.html')

@bp.app_errorhandler(403)
def handle_403(err):
    return render_template('errors/error.html', 
        error='403', 
        message="Internal Server Error. Sorry, that's our fault. Please check back later."), 403

@bp.app_errorhandler(404)
def handle_404(err):
    return render_template('errors/error.html', 
        error='404', 
        message='Page not Found. Check your URL to make sure you typed it in correctly.'), 404

@bp.app_errorhandler(500)
def handle_500(err):
    return render_template('errors/error.html', 
        error='500',
        message="Internal Server Error. Sorry that's our fault. Please check back again later."), 500