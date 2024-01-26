from flask import Flask
from flask import redirect, url_for, session, render_template
from authlib.integrations.flask_client import OAuth
from interga_dev.routes.usuarios import usuarios
from interga_dev.routes.visitantes import visitantes

oauth = OAuth()

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = "VB4028U32683476528594944"
  
  # Configuração do OAuth
  oauth.init_app(app)
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
    jwks_uri='https://www.googleapis.com/oauth2/v3/certs',
    client_kwargs={'scope': 'openid email profile'}
  )
  
  @app.route('/login')
  def login():
    return render_template('login.html')
  
  @app.route('/login-google')
  def login_google():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

  @app.route('/authorize')
  def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo', token=token)
    user_info = resp.json()
    print(user_info)
    
    for key, value in user_info.items():
      session[key] = value
    
    if user_info['name']:
      return redirect(url_for('usuarios.perfil'))
    else:
      session['name'] = 'Usuário não identificado'
      return redirect(url_for('usuarios.perfil'))
  
  # Registrando os blueprints depois de instanciar o objeto OAuth
  app.register_blueprint(usuarios)
  app.register_blueprint(visitantes)
    
  return app
