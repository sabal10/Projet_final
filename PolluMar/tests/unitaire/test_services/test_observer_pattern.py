# ✅ tests/unitaire/test_services/test_observer_pattern.py

from app.services.observers.pollution_report_subject import PollutionReportSubject
from app.services.observers.console_observer import ConsoleObserver
from app.services.observers.email_observer import EmailObserver
import pytest

def test_observer_notification(capsys):
    subject = PollutionReportSubject(report_id=101, description="Déversement d'hydrocarbures")

    console_observer = ConsoleObserver()
    email_observer = EmailObserver()

    subject.attach(console_observer)
    subject.attach(email_observer)

    fake_data = {
        "pollution_type": "Hydrocarbures",
        "location": "Baie de Tadoussac",
        "responder_email": "marine@pollumar.ca",
        "status": "Résolu"
    }

    subject.notify(fake_data)

    captured = capsys.readouterr()

    assert "[ConsoleObserver]" in captured.out
    assert "[EmailObserver]" in captured.out  # ✅ Correction ici
