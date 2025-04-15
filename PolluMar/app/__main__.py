# app/__main__.py

from flask import Flask
from app.views.index_routes import index_bp

app = Flask(__name__)

# Enregistrer la route de la page d'accueil
app.register_blueprint(index_bp)

if __name__ == '__main__':
    app.run(debug=True)
