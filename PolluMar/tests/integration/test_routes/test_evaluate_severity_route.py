import sys
import os
import pytest
from unittest.mock import patch

# 📦 Ajout du chemin racine pour que "app" soit importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from app import create_app

# ✅ Création d’un client Flask en mode test
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# ✅ Test de la route POST /evaluate_severity avec données valides
@patch("app.views.report_routes.SeverityEvaluator.evaluate")
def test_evaluate_severity_route_success(mock_evaluate, client):
    # Simule un retour "Urgent" peu importe les données
    mock_evaluate.return_value = "Urgent"

    data = {
        "pollution_type": "Plastiques",
        "quantity": 80.0
    }

    response = client.post("/evaluate_severity", json=data)

    # ✅ Vérifie la réponse HTTP
    assert response.status_code == 200

    # ✅ Vérifie le format de la réponse
    json_data = response.get_json()
    assert "severity" in json_data
    assert json_data["severity"] == "Urgent"

    # ✅ Vérifie que l’évaluation a bien été appelée
    mock_evaluate.assert_called_once_with("Plastiques", 80.0)
