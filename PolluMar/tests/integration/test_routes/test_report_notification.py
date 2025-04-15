import sys
import os
import pytest
from unittest.mock import patch

# 📦 Ajout du chemin racine du projet
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# ✅ Test 1 : vérifie l'évaluation correcte de la gravité
def test_evaluate_severity_route(client):
    response = client.post("/evaluate_severity", json={
        "pollution_type": "Déchets Chimiques",
        "quantity": 300  # ➤ quantité entre 100 et 500 = "Modéré"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "severity" in data
    assert data["severity"] == "Modéré"  # ✅ attendue selon ta logique

# ✅ Test 2 : vérifie que la gravité est "Urgent" si > 500
def test_evaluate_severity_urgent(client):
    response = client.post("/evaluate_severity", json={
        "pollution_type": "Déchets Chimiques",
        "quantity": 600
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["severity"] == "Urgent"

# ✅ Test 3 : vérifie le comportement avec un type inconnu
def test_evaluate_severity_unknown(client):
    response = client.post("/evaluate_severity", json={
        "pollution_type": "Boue Toxique",
        "quantity": 42
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["severity"] == "Inconnue"
