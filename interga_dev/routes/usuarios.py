from flask import Blueprint, redirect, url_for, session, render_template

usuarios = Blueprint('usuarios', __name__, url_prefix='/usuario')

@usuarios.route('/perfil')
def perfil():
  return render_template('usuarios/home.html')

