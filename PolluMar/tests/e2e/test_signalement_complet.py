import sys
import os
import pytest
from unittest.mock import patch

# 📦 Ajoute le chemin racine du projet
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("app.views.report_routes.NotificationService.send")
@patch("app.views.report_routes.Database.execute_query")
def test_signalement_complet_e2e(mock_execute, mock_send, client):
    # 1️⃣ Évaluation de la gravité
    data_eval = {
        "pollution_type": "Déchets Chimiques",
        "quantity": 150.0
    }

    response_eval = client.post("/evaluate_severity", json=data_eval)
    assert response_eval.status_code == 200
    severity = response_eval.get_json().get("severity")
    assert severity in ["Faible", "Modéré", "Urgent"]

    # 2️⃣ Notification après évaluation
    data_signalement = {
        "name": "Michel Expert",
        "pollution_type": data_eval["pollution_type"],
        "description": "Fuite de produits chimiques",
        "location": "Site Industriel Z3",
        "quantity": data_eval["quantity"],
        "responder_name": "Surveillant Régional",
        "responder_email": "surveillance@region.ca"
    }

    response_notify = client.post("/send_notification", json=data_signalement)
    assert response_notify.status_code == 200

    json_data = response_notify.get_json()
    assert "message" in json_data
    assert "notification envoyée" in json_data["message"]

    # ✅ Vérifie que la notification a été appelée
    assert mock_send.called
    assert mock_execute.called
