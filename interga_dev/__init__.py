from flask import Flask
from authlib.integrations.flask_client import OAuth

def create_app():
  app = Flask(__name__)
  
  from interga_dev.routes.usuario import user
  from interga_dev.routes.visitante import guest
  
  app.register_blueprint(user)
  app.register_blueprint(guest)

  # Configuração do OAuth
  oauth = OAuth(app)
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
  
  return app
