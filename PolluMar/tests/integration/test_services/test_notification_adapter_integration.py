# 📁 tests/integration/test_services/test_notification_adapter_integration.py

import pytest
from datetime import datetime
from app.services.notification_service import NotificationService

BASE_DATA = {
    "name": "Test Alert",
    "pollution_type": "Déchets Chimiques",
    "description": "Test de fuite",
    "quantity": 120,
    "responder_name": "Inspecteur Test",
    "responder_email": "testeur@pollumar.ca",
}

@pytest.mark.parametrize("channel,expected", [
    ("console", "[Console]"),
    ("email", "[Email]"),
    ("sms", "[SMS]")
])
def test_notification_service_uses_correct_adapter(channel, expected, capsys):
    """
    Teste que NotificationService utilise bien l'adaptateur correct en fonction du canal.
    """
    # Données uniques pour éviter les doublons
    data = dict(BASE_DATA)
    data["location"] = f"Zone {channel}-{datetime.now().timestamp()}"  # 🔁 Unique à chaque test
    data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    service = NotificationService(channel)
    result = service.send(data)
    output = capsys.readouterr().out

    assert expected in output
    assert result == "Notification envoyée"
