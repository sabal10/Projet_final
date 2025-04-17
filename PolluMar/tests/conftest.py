# 📁 tests/conftest.py

import pytest
from app.models.database import Database
from app.__main__ import app  # ✅ Import corrigé : évite le conflit avec le dossier app/

@pytest.fixture
def client():
    """
    Client de test Flask pour les tests d’intégration.
    """
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def clean_up_after_test():
    """
    Fixture automatique exécutée après chaque test.
    Elle supprime tous les signalements de test créés par les E2E ou intégration.
    """
    yield
    db = Database()
    db.execute_query("""
        DELETE FROM reports
        WHERE responder_name LIKE 'Agent E2E%'
           OR responder_name LIKE 'Inspecteur Test%'
           OR responder_name LIKE 'Agent Test%'
           OR location LIKE 'Zone-E2E-%'
           OR location LIKE 'Zone %'
    """)
