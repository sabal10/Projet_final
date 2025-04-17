# 📁 tests/e2e/test_notification_adapter_e2e.py

import pytest
from app import create_app
from flask.testing import FlaskClient
from datetime import datetime

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

@pytest.mark.parametrize("channel, expected_message, expected_prefix", [
    ("console", "Notification envoyée", "[Console]"),
    ("email", "Notification envoyée", "[Email]"),
    ("sms", "Notification envoyée", "[SMS]")
])
def test_report_route_with_adapter(client: FlaskClient, channel, expected_message, expected_prefix, capsys):
    """
    Test E2E : vérifie que /report déclenche la notification via le bon adaptateur.
    """
    payload = {
        "name": "Test Adapter E2E",
        "pollution_type": "Plastiques",
        "description": "Simulation E2E",
        "location": f"Zone-E2E-{channel}-{datetime.now().timestamp()}",
        "quantity": 60,
        "severity": "Inconnue",
        "responder_name": "Agent E2E",
        "responder_email": "agent-e2e@pollumar.ca",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "channel": channel
    }

    response = client.post("/report", json=payload)
    output = capsys.readouterr().out

    assert response.status_code == 200
    assert response.get_json()["message"] == expected_message
    assert expected_prefix in output  # ✅ Recherché explicitement
