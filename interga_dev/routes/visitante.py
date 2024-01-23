from flask import redirect, url_for, render_template, session
from flask import Blueprint

guest = Blueprint('guest', __name__, url_prefix='/')

@guest.route('')
@guest.route('/login')
def login():
  return render_template('login.html')