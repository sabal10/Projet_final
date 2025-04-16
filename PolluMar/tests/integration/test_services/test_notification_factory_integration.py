import pytest
from app.services.notification_service import NotificationService
from datetime import datetime
from uuid import uuid4

# 🔧 Génère des données uniques pour éviter les doublons
def generate_data(source: str) -> dict:
    unique = uuid4().hex[:6]
    return {
        "name": f"Testeur {source} {unique}",
        "pollution_type": "Hydrocarbures",
        "description": f"Pollution simulée via {source}",
        "location": f"Zone {unique}",
        "quantity": 45.0,
        "responder_name": "Inspecteur Marin",
        "responder_email": f"testeur_{unique}@pollumar.ca",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def test_send_notification_console(capsys):
    service = NotificationService(channel="console")
    data = generate_data("Console")
    service.send(data)

    captured = capsys.readouterr()
    assert "[Console] Notification envoyée à Inspecteur Marin" in captured.out

def test_send_notification_email(capsys):
    service = NotificationService(channel="email")
    data = generate_data("Email")
    service.send(data)

    captured = capsys.readouterr()
    assert "[Email] Objet: Alerte Pollution" in captured.out

def test_send_notification_sms(capsys):
    service = NotificationService(channel="sms")
    data = generate_data("SMS")
    service.send(data)

    captured = capsys.readouterr()
    assert "[SMS] Envoi à Inspecteur Marin" in captured.out
