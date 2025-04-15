# Ce fichier définit une classe Singleton pour gérer la base de données SQLite,
# en garantissant une instance unique et une initialisation sûre.

import sqlite3
import os

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)

            #  Construction du chemin absolu vers pollution.db (robuste)
            base_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(base_dir, "..", "..", "pollution.db")

            cls._instance.conn = sqlite3.connect(db_path, check_same_thread=False)
            cls._instance.cursor = cls._instance.conn.cursor()

        return cls._instance

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

#  Exposition globale : rétrocompatibilité avec le reste du code
db = Database()
conn = db.conn
cursor = db.cursor

#  Initialisation de la base uniquement si ce fichier est exécuté directement
if __name__ == "__main__":
    db.execute_query("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            pollution_type TEXT,
            description TEXT,
            location TEXT,
            quantity REAL,
            severity TEXT,
            status TEXT,
            media TEXT,
            responder_name TEXT,
            responder_email TEXT,
            created_at TEXT,
            resolved_at TEXT,
            comment TEXT
        )
    """)
    print(" Base de données initialisée avec succès.")