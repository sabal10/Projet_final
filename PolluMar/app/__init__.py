# 📁 app/__init__.py

from flask import Flask

# Importation des blueprints existants
from app.views.index_routes import index_bp
from app.views.about_routes import about_bp
from app.views.manage_routes import manage_bp
from app.views.report_routes import report_bp
from app.views.evaluate_severity_routes import evaluate_bp  # ✅ Nouveau blueprint pour /evaluate_severity

def create_app():
    app = Flask(__name__)

    # Enregistrement des blueprints
    app.register_blueprint(index_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(manage_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(evaluate_bp)  # ✅ Activation du nouveau blueprint

    return app
