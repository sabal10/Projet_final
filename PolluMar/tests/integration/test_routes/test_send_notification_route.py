import sys
import os
import pytest
from unittest.mock import patch

# 📦 Ajout du chemin racine du projet pour permettre les imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from app import create_app

# ✅ Création du client Flask pour le test
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# ✅ Test de la route POST /send_notification
@patch("app.views.report_routes.NotificationService.send")
@patch("app.views.report_routes.SeverityEvaluator.evaluate")
@patch("app.views.report_routes.Database.execute_query")
def test_send_notification_route_success(mock_execute, mock_evaluate, mock_send, client):
    # Simule un niveau de gravité "Urgent"
    mock_evaluate.return_value = "Urgent"
    
    # Simule que l'insertion SQL réussit
    mock_execute.return_value = None

    data = {
        "name": "Alice",
        "pollution_type": "Hydrocarbures",
        "description": "Déversement près du quai",
        "location": "Quai Sud",
        "quantity": 12.5,
        "responder_name": "Inspecteur Rivière",
        "responder_email": "inspecteur@ville.ca"
    }

    response = client.post("/send_notification", json=data)

    # ✅ La requête doit réussir
    assert response.status_code == 200

    # ✅ Le message doit être présent dans la réponse JSON
    json_data = response.get_json()
    assert "message" in json_data
    assert "notification envoyée" in json_data["message"]

    # ✅ Vérifie les appels aux mocks
    mock_evaluate.assert_called_once_with("Hydrocarbures", 12.5)
    mock_execute.assert_called()
    mock_send.assert_called_once_with(data)
