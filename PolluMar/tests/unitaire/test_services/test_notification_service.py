import sys
import os
from unittest.mock import patch
import pytest
from datetime import datetime

# Ajout du dossier racine (PolluMar) pour permettre l'import de app.*
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from app.services.notification_service import NotificationService

# 🔁 Données valides utilisées dans tous les tests
VALID_DATA = {
    "name": "Jean Dupont",
    "pollution_type": "Plastiques",
    "description": "Pollution plastique importante",
    "location": "Port de Sherbrooke",
    "quantity": 42.0,
    "responder_name": "Inspecteur Environnement",
    "responder_email": "inspecteur@ville.ca",
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # ✅ Ajout ici
}

# ✅ Test 1 : Envoi avec données valides → insertion réussie
@patch("app.services.notification_service.Database")
def test_send_notification_success(mock_db_class):
    service = NotificationService()
    mock_db = mock_db_class.return_value

    # Simule l’absence de doublon → on autorise l’insertion
    mock_db.execute_query.side_effect = [[], None]

    service.send(VALID_DATA)

    # On attend 2 appels : SELECT doublon + INSERT
    assert mock_db.execute_query.call_count == 2


# ✅ Test 2 : Donnée invalide (champ manquant) → exception levée
def test_send_notification_missing_field():
    service = NotificationService()
    invalid_data = VALID_DATA.copy()
    del invalid_data["location"]  # ❌ Supprime un champ requis

    with pytest.raises(ValueError) as exc_info:
        service.send(invalid_data)

    assert "Champ obligatoire manquant" in str(exc_info.value)


# ✅ Test 3 : Doublon détecté → pas d’insertion
@patch("app.services.notification_service.Database")
def test_send_notification_duplicate(mock_db_class):
    service = NotificationService()
    mock_db = mock_db_class.return_value

    # Simule la détection d’un doublon (SELECT retourne une ligne)
    mock_db.execute_query.side_effect = [[{"id": 1}]]

    service.send(VALID_DATA)

    # Un seul appel attendu (SELECT doublon)
    assert mock_db.execute_query.call_count == 1
