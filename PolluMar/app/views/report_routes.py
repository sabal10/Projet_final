# 📁 app/views/report_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from datetime import datetime
from app.models.database import Database
from app.services.notification_service import NotificationService
from app.services.severity_evaluator import SeverityEvaluator

from app.services.commands.send_notification_command import SendNotificationCommand
from app.services.commands.command_invoker import CommandInvoker

report_bp = Blueprint("report", __name__)

# ✅ Route GET : affichage du formulaire
@report_bp.route("/report")
def show_report():
    return render_template("pages/report.html")


# ✅ Route POST : formulaire HTML ou JSON
@report_bp.route("/report", methods=["POST"])
def report():
    if request.is_json:
        form_data = request.get_json()
    else:
        form_data = request.form.to_dict()

    form_data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form_data["source"] = "formulaire"
    form_data["status"] = "En attente"

    # ✅ Définir channel si absent
    form_data["channel"] = form_data.get("channel", "console")

    evaluator = SeverityEvaluator()
    form_data["severity"] = evaluator.evaluate(
        form_data["pollution_type"],
        float(form_data["quantity"])
    )

    service = NotificationService(channel=form_data["channel"])
    service.send(form_data)

    if request.is_json:
        return jsonify({"message": "Notification envoyée"})
    return redirect(url_for("report.show_report"))


# ✅ Gravité dynamique AJAX
@report_bp.route("/evaluate_severity", methods=["POST"])
def evaluate_severity():
    data = request.get_json()
    pollution_type = data.get("pollution_type")
    quantity = float(data.get("quantity"))

    evaluator = SeverityEvaluator()
    severity = evaluator.evaluate(pollution_type, quantity)

    return jsonify({"severity": severity})


# ✅ Route AJAX : envoi complet
@report_bp.route("/send_notification", methods=["POST"])
def send_notification():
    data = request.get_json()
    print("📨 Données reçues :", data)

    try:
        data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["source"] = "ajax"
        data["status"] = "En attente"

        # ✅ Définir channel si manquant
        data["channel"] = data.get("channel", "console")

        evaluator = SeverityEvaluator()
        data["severity"] = evaluator.evaluate(
            data["pollution_type"],
            float(data["quantity"])
        )

        service = NotificationService(channel=data["channel"])
        service.send(data)

        return jsonify({"message": "✅ Signalement enregistré et notification envoyée."})

    except Exception as e:
        print("❌ Erreur :", str(e))
        return jsonify({"error": str(e)}), 500


# ✅ Command Pattern : exécution encapsulée
@report_bp.route("/command/send_notification", methods=["POST"])
def command_send_notification():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400

    report = data.get("report")
    if not report:
        return jsonify({"error": "Champ 'report' manquant"}), 400

    report["source"] = report.get("source", "command")
    report["status"] = report.get("status", "En attente")
    report["channel"] = report.get("channel", "console")  # ✅ Sécurité ici aussi

    notification_service = NotificationService(channel=report["channel"])
    command = SendNotificationCommand(notification_service, report)

    invoker = CommandInvoker()
    invoker.add_command(command)
    invoker.run()

    return jsonify({"message": "Commande exécutée avec succès"}), 200
