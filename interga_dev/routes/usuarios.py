from flask import redirect, url_for, render_template, request, session
from flask import Blueprint

users = Blueprint('users', __name__, url_prefix='/usuarios')


@users.route('/login')
def login():
  return render_template('login.html')

@users.route('/logout')
def logout():
  # handle logout request
  pass