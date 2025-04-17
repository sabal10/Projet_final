# 📁 app/views/report_routes.py

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


# ✅ Route POST : signalement manuel via formulaire HTML ou appel JSON (ex: test ou AJAX)
@report_bp.route("/report", methods=["POST"])
def report():
    """
    Traite un nouveau signalement soumis soit via le formulaire HTML, soit via une requête JSON.
    Évalue la gravité, insère les données, et déclenche la notification.
    """
    # 🔄 Compatibilité HTML (formulaire) ou JSON (test / JS)
    if request.is_json:
        form_data = request.get_json()
    else:
        form_data = request.form.to_dict()

    # 🕒 Date d'enregistrement sécurisée côté serveur
    form_data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 🔍 Gravité évaluée dynamiquement avec le pattern Strategy
    evaluator = SeverityEvaluator()
    form_data["severity"] = evaluator.evaluate(
        form_data["pollution_type"],
        float(form_data["quantity"])
    )

    # 📡 Notification envoyée via NotificationService (Factory + Adapter)
    service = NotificationService(channel=form_data.get("channel", "console"))
    service.send(form_data)

    # 🔁 Retour JSON pour AJAX ou redirection HTML classique
    if request.is_json:
        return jsonify({"message": "Notification envoyée"})
    return redirect(url_for("report.show_report"))


# ✅ Route POST : API pour évaluer dynamiquement la gravité (AJAX uniquement)
@report_bp.route("/evaluate_severity", methods=["POST"])
def evaluate_severity():
    """
    Évalue dynamiquement la gravité selon le type et la quantité (utilisé côté client via AJAX).
    """
    data = request.get_json()
    pollution_type = data.get("pollution_type")
    quantity = float(data.get("quantity"))

    evaluator = SeverityEvaluator()
    severity = evaluator.evaluate(pollution_type, quantity)

    return jsonify({"severity": severity})


# ✅ Route POST : API pour envoyer une notification complète (AJAX ou usage scripté)
@report_bp.route("/send_notification", methods=["POST"])
def send_notification():
    """
    Enregistre un signalement et envoie une notification complète via appel JSON.
    """
    data = request.get_json()
    print("📨 Données reçues :", data)

    try:
        # ⏱️ Ajout de la date serveur (sécurité)
        data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 🧠 Gravité calculée si non fournie
        evaluator = SeverityEvaluator()
        data["severity"] = evaluator.evaluate(
            data["pollution_type"],
            float(data["quantity"])
        )

        # 📨 Envoi via le service centralisé
        service = NotificationService(channel=data.get("channel", "console"))
        service.send(data)

        return jsonify({"message": "✅ Signalement enregistré et notification envoyée."})

    except Exception as e:
        print("❌ Erreur :", str(e))
        return jsonify({"error": str(e)}), 500
