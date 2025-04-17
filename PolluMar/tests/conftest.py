# 📁 tests/conftest.py

import pytest
from app.models.database import Database

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
           OR location LIKE 'Zone-E2E-%'
           OR location LIKE 'Zone %'
    """)
