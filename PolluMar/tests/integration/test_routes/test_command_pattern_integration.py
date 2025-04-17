# 📁 tests/integration/test_routes/test_command_pattern_integration.py

import json
from datetime import datetime
from app import create_app
import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_command_send_notification(client):
    # ✅ Données simulées pour la commande avec created_at
    payload = {
        "report": {
            "name": "Test Integration Command",
            "pollution_type": "Plastiques",
            "description": "Test intégration via commande",
            "location": "Zone X",
            "quantity": "12",
            "responder_name": "Agent Test Command",
            "responder_email": "test@command.com",
            "channel": "console",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }

    response = client.post(
        "/command/send_notification",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 200
    assert "Commande exécutée avec succès" in response.get_json()["message"]
