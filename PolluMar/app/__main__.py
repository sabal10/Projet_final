import sys
import os

# 👉 Corrige les erreurs d'import en ajoutant la racine du projet au path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from app.views.index_routes import index_bp
from app.views.about_routes import about_bp
from app.views.manage_routes import manage_bp
from app.views.report_routes import report_bp
from app.views.history_routes import history_bp
from app.views.dashboard_routes import dashboard_bp
from app.views.evaluate_severity_routes import evaluate_bp  # ✅ ajout pour la gravité

app = Flask(__name__)

# Enregistrement des blueprints
app.register_blueprint(index_bp)
app.register_blueprint(about_bp)
app.register_blueprint(manage_bp)
app.register_blueprint(report_bp)
app.register_blueprint(history_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(evaluate_bp)  # ✅ enregistrement de la route POST /evaluate_severity

if __name__ == "__main__":
    app.run(debug=True)
