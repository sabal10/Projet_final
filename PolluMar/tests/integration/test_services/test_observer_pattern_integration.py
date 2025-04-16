# 📁 tests/integration/test_services/test_observer_pattern_integration.py

import pytest
from app.services.observers.pollution_report_subject import PollutionReportSubject
from app.services.observers.console_observer import ConsoleObserver
from app.services.observers.email_observer import EmailObserver

def test_pollution_report_resolution_notifies_observers(capsys):
    # Création du sujet avec identifiant et description
    subject = PollutionReportSubject(report_id=404, description="Déversement chimique dans le port de Québec")

    # Création des observateurs
    console_observer = ConsoleObserver()
    email_observer = EmailObserver()

    # Attachement des observateurs au sujet
    subject.attach(console_observer)
    subject.attach(email_observer)

    # Résolution de l'incident (déclenche la notification)
    subject.resolve()

    # Capture de la sortie console
    captured = capsys.readouterr()

    # Vérification de la présence des messages des observateurs
    assert "[ConsoleObserver]" in captured.out
    assert "[EmailObserver]" in captured.out
    assert "Signalement #404 résolu" in captured.out
