from flask import Blueprint, render_template, request
from app.models.database import Database

# ✅ Déclaration du blueprint
history_bp = Blueprint("history", __name__)

@history_bp.route("/history")
def show_history():
    db = Database()

    # 🔍 Récupération des filtres (optionnels)
    type_filter = request.args.get("type")
    severity_filter = request.args.get("severity")

    # 🧱 Construction dynamique de la requête (par défaut : incidents Résolus)
    base_query = "SELECT * FROM reports WHERE status = 'Résolu'"
    params = []

    if type_filter:
        base_query += " AND pollution_type = ?"
        params.append(type_filter)
    if severity_filter:
        base_query += " AND severity = ?"
        params.append(severity_filter)

    # 📦 Exécution
    rows = db.execute_query(base_query, params)

    # 🔁 Transformation en dictionnaire pour Jinja2
    reports = [dict(zip([col[0] for col in db.cursor.description], row)) for row in rows]

    for r in reports:
        print(f"[DEBUG] ID: {r['id']}, Created At: {r['created_at']}")

    return render_template("pages/history.html", reports=reports)
