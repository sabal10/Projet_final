# app/views/dashboard_routes.py

from flask import Blueprint, render_template
from app.models.database import Database

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def show_dashboard():
    db = Database()

    total = db.execute_query("SELECT COUNT(*) FROM reports")[0][0]
    en_cours = db.execute_query("SELECT COUNT(*) FROM reports WHERE status != 'Résolu'")[0][0]
    resolus = db.execute_query("SELECT COUNT(*) FROM reports WHERE status = 'Résolu'")[0][0]

    # 📊 Données pour les graphiques
    rows = db.execute_query("SELECT pollution_type FROM reports")
    pollution_types = [row[0] for row in rows]

    labels = ["Plastiques", "Hydrocarbures", "Déchets Chimiques"]
    values = [pollution_types.count(label) for label in labels]

    return render_template(
        "pages/dashboard.html",
        total=total,
        en_cours=en_cours,
        resolus=resolus,
        labels=labels,
        values=values
    )
