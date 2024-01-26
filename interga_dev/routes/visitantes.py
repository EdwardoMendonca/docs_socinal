from flask import redirect, url_for, render_template, session
from flask import Blueprint

visitantes = Blueprint('visitantes', __name__, url_prefix='/')

@visitantes.route('')
@visitantes.route('/home')
def home():
  return render_template('home.html')