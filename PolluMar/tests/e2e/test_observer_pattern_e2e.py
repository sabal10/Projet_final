# 📁 tests/e2e/test_observer_pattern_e2e.py

import pytest
from app.services.observers.pollution_report_subject import PollutionReportSubject
from app.services.observers.console_observer import ConsoleObserver
from app.services.observers.email_observer import EmailObserver

def test_full_observer_flow_on_pollution_report(capsys):
    """
    Test end-to-end : création, attachement, résolution et vérification des notifications.
    """

    # Étape 1 : Création d’un signalement simulé
    report = PollutionReportSubject(
        report_id=2025,
        description="Fuite de plastique dans le fleuve Saint-Laurent"
    )

    # Étape 2 : Création des observateurs simulés
    console_logger = ConsoleObserver()
    email_notifier = EmailObserver()

    # Étape 3 : Enregistrement des observateurs
    report.attach(console_logger)
    report.attach(email_notifier)

    # Étape 4 : Simulation de la résolution du signalement
    report.resolve()

    # Étape 5 : Capture des notifications
    captured = capsys.readouterr()

    # Étape 6 : Vérifications globales
    assert "Signalement #2025 résolu" in captured.out
    assert "[ConsoleObserver]" in captured.out
    assert "[EmailObserver]" in captured.out
    assert "Saint-Laurent" in captured.out
