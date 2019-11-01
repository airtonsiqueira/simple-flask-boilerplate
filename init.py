import os

from flask import Flask, render_template

import server.keys
import server.config

# Instância do app
app = Flask(
    __name__,
    template_folder="client/templates",
    static_folder="client/static",
)
# from routes import routes_blueprint
from server.routes import routes_blueprint
app.register_blueprint(routes_blueprint)

# Exemplo de import de modelo
import server.models.user

UPLOAD_FOLDER = 'client/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(debug=True)
