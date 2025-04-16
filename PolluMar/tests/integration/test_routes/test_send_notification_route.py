import sys
import os
from datetime import datetime
import pytest
from unittest.mock import patch

# 📦 Chemin d'import racine
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("app.views.report_routes.NotificationService.send")
@patch("app.views.report_routes.SeverityEvaluator.evaluate")
def test_send_notification_route_success(mock_evaluate, mock_send, client):
    mock_evaluate.return_value = "Urgent"
    
    data = {
        "name": "Alice",
        "pollution_type": "Hydrocarbures",
        "description": "Déversement près du quai",
        "location": "Quai Sud",
        "quantity": 12.5,
        "responder_name": "Inspecteur Rivière",
        "responder_email": "inspecteur@ville.ca",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    response = client.post("/send_notification", json=data)

    assert response.status_code == 200
    json_data = response.get_json()
    assert "message" in json_data
    assert "notification envoyée" in json_data["message"]

    mock_evaluate.assert_called_once_with("Hydrocarbures", 12.5)
    assert mock_send.called
