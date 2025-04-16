# 📁 Fichier : app/views/report_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from datetime import datetime
from app.models.database import Database
from app.services.notification_service import NotificationService
from app.services.severity_evaluator import SeverityEvaluator

report_bp = Blueprint("report", __name__)

# ✅ Route GET : affichage du formulaire de signalement (interface utilisateur)
@report_bp.route("/report")
def show_report():
    return render_template("pages/report.html")


# ✅ Route POST (formulaire HTML) : signalement manuel via le formulaire
@report_bp.route("/report", methods=["POST"])
def report():
    form_data = request.form.to_dict()

    # 🔁 Ajout de la date de création générée dynamiquement (sécurité backend)
    form_data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ✅ Évaluation de la gravité via Strategy Pattern
    evaluator = SeverityEvaluator()
    form_data["severity"] = evaluator.evaluate(
        form_data["pollution_type"],
        float(form_data["quantity"])
    )

    # ✅ Insertion et notification
    service = NotificationService()
    service.send(form_data)

    return redirect(url_for("report.show_report"))


# ✅ Route POST (JSON) : évaluation dynamique de la gravité (AJAX)
@report_bp.route("/evaluate_severity", methods=["POST"])
def evaluate_severity():
    data = request.get_json()

    pollution_type = data.get("pollution_type")
    quantity = float(data.get("quantity"))

    evaluator = SeverityEvaluator()
    severity = evaluator.evaluate(pollution_type, quantity)

    return jsonify({"severity": severity})


# ✅ Route POST (JSON) : signalement via JavaScript (AJAX)
@report_bp.route("/send_notification", methods=["POST"])
def send_notification():
    data = request.get_json()
    print("📨 Données reçues :", data)

    try:
        # 🔁 Ajout dynamique de la date côté serveur
        data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 🧠 Calcul de la gravité via Strategy Pattern
        evaluator = SeverityEvaluator()
        data["severity"] = evaluator.evaluate(
            data["pollution_type"],
            float(data["quantity"])
        )

        # ✅ Insertion et notification centralisée via le service
        service = NotificationService()
        service.send(data)

        return jsonify({"message": "✅ Signalement enregistré et notification envoyée."})

    except Exception as e:
        print("❌ Erreur :", str(e))
        return jsonify({"error": str(e)}), 500
