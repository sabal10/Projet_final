import sys
import os
import pytest
from unittest.mock import patch

# 🔧 Ajout du chemin racine du projet
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from app import create_app

# ✅ Création du client Flask pour les tests
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# ✅ Test de la route /report
@patch("app.views.report_routes.NotificationService.send")
def test_report_route_success(mock_send, client):
    form_data = {
        "name": "Jean Dupont",
        "pollution_type": "Plastiques",
        "description": "Sacs plastiques sur la rive",
        "location": "Plage Est",
        "quantity": 30.0,
        "responder_name": "Inspecteur",
        "responder_email": "inspecteur@environnement.ca",
        "severity": "Modéré"
    }

    # Envoi de la requête POST
    response = client.post("/report", data=form_data, follow_redirects=True)

    # ✅ Vérifie le code réponse
    assert response.status_code in (200, 302)

    # ✅ Vérifie que la méthode NotificationService.send a été appelée
    assert mock_send.called
