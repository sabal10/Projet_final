# 📁 app/views/index_routes.py

from flask import Blueprint, render_template
from app.models.database import Database

index_bp = Blueprint("home", __name__)

@index_bp.route("/")
def home():
    db = Database()
    
    # ✅ Récupère tous les signalements "En attente", quelle que soit la source
    rows = db.execute_query("SELECT * FROM reports WHERE status = 'En attente'")
    
    # Conversion en dictionnaires pour l'affichage
    reports = [dict(zip([column[0] for column in db.cursor.description], row)) for row in rows]

    # Statistiques pour le graphique
    labels = ["Plastiques", "Hydrocarbures", "Déchets Chimiques"]
    values = [sum(1 for r in reports if r["pollution_type"] == l) for l in labels]

    return render_template("pages/index.html", reports=reports, labels=labels, values=values)
