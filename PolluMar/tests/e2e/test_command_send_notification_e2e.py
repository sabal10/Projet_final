# 📁 tests/e2e/test_command_send_notification_e2e.py

import json
from datetime import datetime

def test_send_notification_command_e2e(client):
    """
    Test E2E simplifié sans navigateur : envoi d'un signalement complet via /command/send_notification.
    """

    payload = {
        "report": {
            "name": "Incident E2E",
            "pollution_type": "Hydrocarbures",
            "description": "Simulation via test e2e",
            "location": "Zone-E2E-1",
            "quantity": "20",
            "responder_name": "Agent E2E Command",
            "responder_email": "e2e@test.com",
            "channel": "console",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # ✅ Important
        }
    }

    response = client.post(
        "/command/send_notification",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 200
    assert "Commande exécutée avec succès" in response.get_json()["message"]
