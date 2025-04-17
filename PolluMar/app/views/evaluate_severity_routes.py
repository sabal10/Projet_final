# 📁 app/views/evaluate_severity_routes.py

from flask import Blueprint, request, jsonify
from app.services.severity_evaluator import SeverityEvaluator

evaluate_bp = Blueprint("evaluate", __name__)

@evaluate_bp.route("/evaluate_severity", methods=["POST"])
def evaluate_severity():
    """
    Reçoit le type de pollution et la quantité, retourne le niveau de gravité évalué.
    Utilise le pattern Strategy via SeverityEvaluator.
    """
    data = request.get_json()
    pollution_type = data.get("pollution_type")
    quantity = data.get("quantity")

    try:
        quantity = float(quantity)
    except (ValueError, TypeError):
        return jsonify({"error": "Quantité invalide"}), 400

    evaluator = SeverityEvaluator()
    severity = evaluator.evaluate(pollution_type, quantity)

    return jsonify({"severity": severity})
