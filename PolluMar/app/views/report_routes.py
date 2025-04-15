from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.models.database import Database
from app.services.notification_service import NotificationService
from app.services.severity_evaluator import SeverityEvaluator

report_bp = Blueprint("report", __name__)

# ✅ Route GET : affichage du formulaire de signalement
@report_bp.route("/report")
def show_report():
    return render_template("pages/report.html")

# ✅ Route POST : traitement du formulaire (utilisée dans les tests)
@report_bp.route("/report", methods=["POST"])
def report():
    form_data = request.form.to_dict()
    service = NotificationService()
    service.send(form_data)
    return redirect(url_for("report.show_report"))

# ✅ Route POST : évaluation de la gravité via JSON
@report_bp.route("/evaluate_severity", methods=["POST"])
def evaluate_severity():
    data = request.get_json()
    pollution_type = data.get("pollution_type")
    quantity = float(data.get("quantity"))

    evaluator = SeverityEvaluator()
    severity = evaluator.evaluate(pollution_type, quantity)
    return jsonify({"severity": severity})

# ✅ Route POST : enregistrement + notification (JSON, utilisé par JS)
@report_bp.route("/send_notification", methods=["POST"])
def send_notification():
    data = request.get_json()
    print("📨 Données reçues :", data)

    db = Database()

    try:
        # Évaluer la gravité
        evaluator = SeverityEvaluator()
        severity = evaluator.evaluate(data["pollution_type"], float(data["quantity"]))

        # Insérer dans la base de données
        query = """
        INSERT INTO reports (
            name, pollution_type, description, location, quantity, 
            responder_name, responder_email, severity, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            data["name"],
            data["pollution_type"],
            data["description"],
            data["location"],
            data["quantity"],
            data["responder_name"],
            data["responder_email"],
            severity,
            "En attente"
        )
        db.execute_query(query, params)

        # Envoyer la notification
        service = NotificationService()
        service.send(data)

        return jsonify({"message": "✅ Signalement enregistré et notification envoyée."})
    
    except Exception as e:
        print("❌ Erreur :", str(e))
        return jsonify({"error": str(e)}), 500
