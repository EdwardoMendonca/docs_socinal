from flask import redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from flask import Blueprint

# Configuração do OAuth
oauth = OAuth()

usuarios = Blueprint('usuarios', __name__, url_prefix='/usuario')

# Configuração do OAuth para o Google
google = oauth.register(
  name='google',
  client_id="434532814222-4rae9gtph81n2tduflajo2l3cun7bo4s.apps.googleusercontent.com",  # Substitua pelo seu Client ID
  client_secret="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",  # Substitua pelo seu Client Secret  
  access_token_url='https://accounts.google.com/o/oauth2/token',
  access_token_params=None,
  authorize_url='https://accounts.google.com/o/oauth2/auth',
  authorize_params=None,
  api_base_url='https://www.googleapis.com/oauth2/v1/',
  client_kwargs={'scope': 'openid email profile'}
)

@usuarios.route('/login')
def login():
  redirect_uri = url_for('authorize', _external=True)
  return google.authorize_redirect(redirect_uri)

@usuarios.route('/authorize')
def authorize():
  token = google.authorize_access_token()
  resp = google.get('userinfo', token=token)
  user_info = resp.json()
  session['email'] = user_info['email']
  return redirect('/')

@usuarios.route('/logout')
def logout():
  # handle logout request
  pass