from flask import Blueprint, render_template, request, jsonify
from app.models.database import Database
from datetime import datetime

manage_bp = Blueprint("manage", __name__)

@manage_bp.route("/manage")
def show_manage():
    db = Database()
    
    # ✅ Récupère uniquement les signalements à traiter (En attente)
    rows = db.execute_query("SELECT * FROM reports WHERE status = 'En attente'")
    
    reports = [dict(zip([col[0] for col in db.cursor.description], row)) for row in rows]
    return render_template("pages/manage.html", reports=reports)

@manage_bp.route("/resolve/<int:id>", methods=["POST"])
def resolve_report(id):
    db = Database()
    data = request.get_json()
    comment = data.get("comment", "")

    try:
        db.execute_query(
            "UPDATE reports SET status='Résolu', comment=?, resolved_at=? WHERE id=?",
            (comment, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), id)
        )
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
