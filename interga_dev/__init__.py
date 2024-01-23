from flask import Flask
from authlib.integrations.flask_client import OAuth
from interga_dev.routes.usuarios import usuarios
from interga_dev.routes.visitantes import visitantes

def create_app():
  app = Flask(__name__)
  
  

  # Configuração do OAuth
  oauth = OAuth(app)
  
  # Registrando os blueprints depois de instanciar o objeto OAuth
  app.register_blueprint(usuarios)
  app.register_blueprint(visitantes)
    
  return app
