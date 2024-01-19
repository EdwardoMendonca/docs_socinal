from flask import Flask
from interga_dev.routes.usuarios import users

app = Flask(__name__)
app.register_blueprint(users)