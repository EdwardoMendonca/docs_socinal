from flask import redirect, url_for, render_template, session
from flask import Blueprint

visitantes = Blueprint('visitantes', __name__, url_prefix='/')

@visitantes.route('')
@visitantes.route('/login')
def login():
  return render_template('login.html')