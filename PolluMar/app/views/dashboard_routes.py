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

    return render_template(
        "pages/dashboard.html",
        total=total,
        en_cours=en_cours,
        resolus=resolus
    )
