# 📁 tests/unitaire/test_services/test_singleton_database.py

from app.models.database import Database

def test_singleton_returns_same_instance():
    """
    Vérifie que la classe Database implémente correctement le pattern Singleton :
    deux appels successifs doivent retourner exactement la même instance.
    """
    db1 = Database()
    db2 = Database()
    assert db1 is db2, "La classe Database ne respecte pas le pattern Singleton (instances différentes)"

def test_singleton_has_cursor_and_connection():
    """
    Vérifie que l'instance du Singleton expose bien un curseur et une connexion SQLite.
    """
    db = Database()
    assert hasattr(db, "cursor"), "L'instance du Singleton doit avoir un curseur SQLite"
    assert hasattr(db, "conn"), "L'instance du Singleton doit avoir une connexion SQLite"
