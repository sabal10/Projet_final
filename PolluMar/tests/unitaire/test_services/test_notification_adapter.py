import pytest
from app.services.notification_adapter import (
    ConsoleNotificationAdapter,
    EmailNotificationAdapter,
    SMSNotificationAdapter
)

VALID_DATA = {
    "name": "Jean Dupont",
    "pollution_type": "Hydrocarbures",
    "description": "Fuite importante",
    "location": "Port Sud",
    "quantity": 32.5,
    "responder_name": "Inspecteur Vallée",
    "responder_email": "vallee@environnement.ca",
    "created_at": "2025-04-15 20:30:00"
}

def test_console_adapter(capsys):
    adapter = ConsoleNotificationAdapter()
    adapter.send(VALID_DATA)
    output = capsys.readouterr().out
    assert "[Console]" in output
    assert VALID_DATA["responder_name"] in output

def test_email_adapter(capsys):
    adapter = EmailNotificationAdapter()
    adapter.send(VALID_DATA)
    output = capsys.readouterr().out
    assert "[Email]" in output
    assert VALID_DATA["responder_email"] in output

def test_sms_adapter(capsys):
    adapter = SMSNotificationAdapter()
    adapter.send(VALID_DATA)
    output = capsys.readouterr().out
    assert "[SMS]" in output
    assert VALID_DATA["location"] in output
